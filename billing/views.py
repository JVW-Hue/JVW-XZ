from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import json

@login_required
def pricing(request):
    return render(request, 'billing/pricing.html')

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
        'paypal_client_id': 'ARK6NTOx6BYynt7sXT2RXr5L1Wkus7MRwIVRXKdBq-ngBWxcg8q1IR-sRM8oui_wZUMdgAIjLtcpal79'
    })

@csrf_exempt
@require_POST
def paypal_success(request):
    try:
        data = json.loads(request.body)
        plan = data.get('plan')
        payment_id = data.get('paymentID')
        
        if plan in ['premium', 'pro']:
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