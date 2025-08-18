from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Website

@login_required
def dashboard(request):
    websites = Website.objects.filter(user=request.user)
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