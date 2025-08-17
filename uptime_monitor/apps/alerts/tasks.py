from celery import shared_task
from django.contrib.auth import get_user_model
from django.conf import settings
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from twilio.rest import Client
import logging

User = get_user_model()
logger = logging.getLogger(__name__)

@shared_task
def send_alert(user_id, website_id, alert_type):
    try:
        user = User.objects.get(id=user_id)
        website = user.websites.get(id=website_id)
    except (User.DoesNotExist, Exception):
        return
    
    if alert_type == 'down':
        subject = f"🚨 {website.name} is DOWN"
        message = f"Your website {website.name} ({website.url}) is currently down."
    else:
        subject = f"✅ {website.name} is back UP"
        message = f"Your website {website.name} ({website.url}) is back online."
    
    # Send email alert
    send_email_alert.delay(user.email, subject, message)
    
    # Send SMS alert if user has Pro plan and phone number
    if user.can_use_sms() and user.phone_number:
        send_sms_alert.delay(user.phone_number, message)

@shared_task
def send_email_alert(email, subject, message):
    if not settings.SENDGRID_API_KEY:
        logger.warning("SendGrid API key not configured")
        return
    
    try:
        mail = Mail(
            from_email='alerts@uptimemonitor.com',
            to_emails=email,
            subject=subject,
            html_content=f"""
            <div style="font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto;">
                <h2 style="color: #333;">{subject}</h2>
                <p style="font-size: 16px; line-height: 1.5;">{message}</p>
                <p style="color: #666; font-size: 14px;">
                    This alert was sent by your Uptime Monitor. 
                    <a href="https://yourapp.com/dashboard">View Dashboard</a>
                </p>
            </div>
            """
        )
        
        sg = SendGridAPIClient(api_key=settings.SENDGRID_API_KEY)
        response = sg.send(mail)
        logger.info(f"Email sent successfully to {email}")
        
    except Exception as e:
        logger.error(f"Failed to send email to {email}: {str(e)}")

@shared_task
def send_sms_alert(phone_number, message):
    if not settings.TWILIO_ACCOUNT_SID or not settings.TWILIO_AUTH_TOKEN:
        logger.warning("Twilio credentials not configured")
        return
    
    try:
        client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
        
        sms_message = client.messages.create(
            body=message,
            from_='+1234567890',  # Your Twilio phone number
            to=phone_number
        )
        
        logger.info(f"SMS sent successfully to {phone_number}")
        
    except Exception as e:
        logger.error(f"Failed to send SMS to {phone_number}: {str(e)}")