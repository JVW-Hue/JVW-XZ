import requests
import time
from celery import shared_task
from django.utils import timezone
from .models import Website, Check, Incident
from ..alerts.tasks import send_alert

@shared_task
def check_website(website_id):
    try:
        website = Website.objects.get(id=website_id, is_active=True)
    except Website.DoesNotExist:
        return
    
    start_time = time.time()
    is_up = False
    status_code = None
    error_message = ""
    
    try:
        response = requests.get(website.url, timeout=30)
        response_time = (time.time() - start_time) * 1000  # Convert to milliseconds
        status_code = response.status_code
        is_up = 200 <= status_code < 400
        
    except requests.exceptions.RequestException as e:
        response_time = (time.time() - start_time) * 1000
        error_message = str(e)
        is_up = False
    
    # Create check record
    check = Check.objects.create(
        website=website,
        is_up=is_up,
        response_time=response_time,
        status_code=status_code,
        error_message=error_message
    )
    
    # Handle incidents
    last_check = Check.objects.filter(website=website).exclude(id=check.id).first()
    
    if not is_up:
        # Website is down
        if not last_check or last_check.is_up:
            # This is a new incident
            incident = Incident.objects.create(
                website=website,
                started_at=timezone.now()
            )
            # Send alert
            send_alert.delay(website.user.id, website.id, 'down')
    else:
        # Website is up
        if last_check and not last_check.is_up:
            # Incident resolved
            incident = Incident.objects.filter(
                website=website,
                is_resolved=False
            ).first()
            if incident:
                incident.ended_at = timezone.now()
                incident.is_resolved = True
                incident.save()
                # Send recovery alert
                send_alert.delay(website.user.id, website.id, 'up')
    
    return {
        'website_id': website_id,
        'is_up': is_up,
        'response_time': response_time,
        'status_code': status_code
    }

@shared_task
def schedule_all_checks():
    """Schedule checks for all active websites"""
    websites = Website.objects.filter(is_active=True)
    for website in websites:
        check_website.delay(website.id)