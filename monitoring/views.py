from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from .models import Website, UptimeCheck
import requests
from datetime import datetime

def check_website_status(website):
    """Check if a website is online and record the result"""
    try:
        response = requests.get(website.url, timeout=10)
        is_online = response.status_code == 200
        response_time = response.elapsed.total_seconds() * 1000
        
        UptimeCheck.objects.create(
            website=website,
            is_online=is_online,
            response_time=response_time,
            status_code=response.status_code
        )
        
        return {
            'is_online': is_online,
            'response_time': response_time,
            'status_code': response.status_code
        }
    except Exception as e:
        UptimeCheck.objects.create(
            website=website,
            is_online=False,
            response_time=0,
            status_code=0,
            error_message=str(e)
        )
        
        return {
            'is_online': False,
            'response_time': 0,
            'status_code': 0,
            'error': str(e)
        }

@login_required
def dashboard(request):
    websites = Website.objects.filter(user=request.user)
    
    # Check all websites status
    for website in websites:
        check_website_status(website)
    
    return render(request, 'monitoring/dashboard.html', {
        'user': request.user,
        'websites': websites
    })

@login_required
def add_website(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        url = request.POST.get('url', '').strip()
        
        if not name or not url:
            messages.error(request, 'Name and URL are required')
            return render(request, 'monitoring/add_website.html')
        
        if not url.startswith(('http://', 'https://')):
            url = 'https://' + url
        
        try:
            Website.objects.create(
                user=request.user,
                name=name,
                url=url
            )
            messages.success(request, f'Website {name} added successfully!')
            return redirect('dashboard')
        except Exception as e:
            messages.error(request, f'Error adding website: {str(e)}')
    
    return render(request, 'monitoring/add_website.html')

@login_required
def website_detail(request, website_id):
    try:
        website = Website.objects.get(id=website_id, user=request.user)
        recent_checks = website.uptime_checks.all()[:10]
        return render(request, 'monitoring/website_detail.html', {
            'website': website,
            'recent_checks': recent_checks
        })
    except Website.DoesNotExist:
        messages.error(request, 'Website not found')
        return redirect('dashboard')

@login_required
def check_website(request, website_id):
    try:
        website = Website.objects.get(id=website_id, user=request.user)
        result = check_website_status(website)
        return JsonResponse({
            'success': True,
            'is_online': result['is_online'],
            'response_time': result['response_time'],
            'status_code': result['status_code']
        })
    except Website.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'Website not found'})