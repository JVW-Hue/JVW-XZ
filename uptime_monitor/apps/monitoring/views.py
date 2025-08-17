from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.db.models import Avg
from .models import Website, Check, Incident, StatusPage
from .forms import WebsiteForm, StatusPageForm

@login_required
def dashboard(request):
    websites = request.user.websites.all()
    context = {
        'websites': websites,
        'total_websites': websites.count(),
        'can_add_more': websites.count() < request.user.get_monitor_limit(),
    }
    return render(request, 'monitoring/dashboard.html', context)

@login_required
def add_website(request):
    if request.user.websites.count() >= request.user.get_monitor_limit():
        messages.error(request, 'You have reached your monitoring limit. Please upgrade your plan.')
        return redirect('dashboard')
    
    if request.method == 'POST':
        form = WebsiteForm(request.POST)
        if form.is_valid():
            website = form.save(commit=False)
            website.user = request.user
            website.save()
            messages.success(request, 'Website added successfully!')
            return redirect('dashboard')
    else:
        form = WebsiteForm()
    
    return render(request, 'monitoring/add_website.html', {'form': form})

@login_required
def website_detail(request, website_id):
    website = get_object_or_404(Website, id=website_id, user=request.user)
    recent_checks = website.checks.all()[:50]
    incidents = website.incidents.all()[:10]
    
    # Calculate stats
    uptime_24h = website.get_uptime_percentage(1)
    uptime_7d = website.get_uptime_percentage(7)
    uptime_30d = website.get_uptime_percentage(30)
    
    avg_response_time = website.checks.filter(is_up=True).aggregate(
        avg_time=Avg('response_time')
    )['avg_time'] or 0
    
    context = {
        'website': website,
        'recent_checks': recent_checks,
        'incidents': incidents,
        'uptime_24h': uptime_24h,
        'uptime_7d': uptime_7d,
        'uptime_30d': uptime_30d,
        'avg_response_time': round(avg_response_time, 2),
    }
    return render(request, 'monitoring/website_detail.html', context)

@login_required
def delete_website(request, website_id):
    website = get_object_or_404(Website, id=website_id, user=request.user)
    if request.method == 'POST':
        website.delete()
        messages.success(request, 'Website deleted successfully!')
    return redirect('dashboard')

def public_status_page(request, slug):
    status_page = get_object_or_404(StatusPage, slug=slug, is_public=True)
    websites = status_page.user.websites.filter(is_active=True)
    
    website_stats = []
    for website in websites:
        recent_check = website.checks.first()
        website_stats.append({
            'website': website,
            'is_up': recent_check.is_up if recent_check else True,
            'uptime_30d': website.get_uptime_percentage(30),
        })
    
    context = {
        'status_page': status_page,
        'website_stats': website_stats,
    }
    return render(request, 'monitoring/public_status.html', context)

@login_required
def manage_status_page(request):
    if not request.user.can_use_status_page():
        messages.error(request, 'Status pages are only available for Pro users.')
        return redirect('dashboard')
    
    try:
        status_page = request.user.statuspage
    except StatusPage.DoesNotExist:
        status_page = None
    
    if request.method == 'POST':
        form = StatusPageForm(request.POST, instance=status_page)
        if form.is_valid():
            status_page = form.save(commit=False)
            status_page.user = request.user
            status_page.save()
            messages.success(request, 'Status page updated successfully!')
            return redirect('manage_status_page')
    else:
        form = StatusPageForm(instance=status_page)
    
    context = {
        'form': form,
        'status_page': status_page,
    }
    return render(request, 'monitoring/manage_status_page.html', context)