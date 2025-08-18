import stripe
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import json
import requests

stripe.api_key = settings.STRIPE_SECRET_KEY

@login_required
def pricing(request):
    return render(request, 'billing/pricing.html')

@login_required
def create_checkout_session(request, plan):
    if plan not in ['premium', 'pro']:
        messages.error(request, 'Invalid plan selected.')
        return redirect('pricing')
    
    price_ids = {
        'premium': 'price_premium_monthly',  # Replace with actual Stripe price IDs
        'pro': 'price_pro_monthly',
    }
    
    try:
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price': price_ids[plan],
                'quantity': 1,
            }],
            mode='subscription',
            success_url=request.build_absolute_uri('/billing/success/'),
            cancel_url=request.build_absolute_uri('/billing/pricing/'),
            customer_email=request.user.email,
            metadata={
                'user_id': request.user.id,
                'plan': plan,
            }
        )
        return redirect(checkout_session.url)
    except Exception as e:
        messages.error(request, 'Error creating checkout session.')
        return redirect('pricing')

@login_required
def success(request):
    messages.success(request, 'Subscription activated successfully!')
    return redirect('dashboard')

@login_required
def paypal_checkout(request, plan):
    if plan not in ['premium', 'pro']:
        messages.error(request, 'Invalid plan selected.')
        return redirect('pricing')
    
    prices = {'premium': '9.00', 'pro': '19.00'}
    plan_names = {'premium': 'Premium Plan', 'pro': 'Pro Plan'}
    
    return render(request, 'billing/paypal_checkout.html', {
        'plan': plan,
        'plan_name': plan_names[plan],
        'price': prices[plan],
        'paypal_client_id': settings.PAYPAL_CLIENT_ID
    })

@csrf_exempt
@require_POST
def paypal_success(request):
    try:
        data = json.loads(request.body)
        plan = data.get('plan')
        payment_id = data.get('paymentID')
        payer_id = data.get('payerID')
        
        if plan in ['premium', 'pro']:
            # Update user plan (you can add a plan field to User model)
            # For now, we'll use session to track the plan
            request.session['user_plan'] = plan
            request.session['payment_id'] = payment_id
            
        return JsonResponse({
            'status': 'success',
            'redirect_url': '/billing/paypal-success-page/'
        })
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)})

@login_required
def paypal_success_page(request):
    plan = request.session.get('user_plan', 'free')
    payment_id = request.session.get('payment_id', '')
    
    return render(request, 'billing/paypal_success.html', {
        'plan': plan,
        'payment_id': payment_id
    })

@csrf_exempt
@require_POST
def stripe_webhook(request):
    payload = request.body
    sig_header = request.META.get('HTTP_STRIPE_SIGNATURE')
    endpoint_secret = settings.STRIPE_WEBHOOK_SECRET
    
    try:
        event = stripe.Webhook.construct_event(payload, sig_header, endpoint_secret)
    except ValueError:
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError:
        return HttpResponse(status=400)
    
    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        user_id = session['metadata']['user_id']
        plan = session['metadata']['plan']
        
        try:
            from django.contrib.auth import get_user_model
            User = get_user_model()
            user = User.objects.get(id=user_id)
            user.plan = plan
            user.stripe_customer_id = session['customer']
            user.save()
        except User.DoesNotExist:
            pass
    
    return HttpResponse(status=200)