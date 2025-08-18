from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.models import User
from django.db import IntegrityError

def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password1 = request.POST.get('password1', '')
        password2 = request.POST.get('password2', '')
        
        if not username or not password1 or not password2:
            messages.error(request, 'All fields are required')
            return render(request, 'registration/signup.html')
            
        if password1 != password2:
            messages.error(request, 'Passwords do not match')
            return render(request, 'registration/signup.html')
        
        try:
            from django.contrib.auth.models import User
            user = User.objects.create_user(username=username, password=password1)
            from django.contrib.auth import login
            login(request, user)
            messages.success(request, 'Account created successfully!')
            return redirect('dashboard')
        except Exception as e:
            messages.error(request, 'Username already exists or invalid')
            return render(request, 'registration/signup.html')
    
    return render(request, 'registration/signup.html')