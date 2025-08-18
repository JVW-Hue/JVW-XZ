from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required

def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        email = request.POST.get('email', '').strip()
        password1 = request.POST.get('password1', '')
        password2 = request.POST.get('password2', '')
        
        # Basic validation
        if not username or not password1 or not password2:
            messages.error(request, 'Username and passwords are required')
            return render(request, 'registration/signup.html')
            
        if len(username) < 3:
            messages.error(request, 'Username must be at least 3 characters')
            return render(request, 'registration/signup.html')
            
        if len(password1) < 6:
            messages.error(request, 'Password must be at least 6 characters')
            return render(request, 'registration/signup.html')
            
        if password1 != password2:
            messages.error(request, 'Passwords do not match')
            return render(request, 'registration/signup.html')
        
        try:
            # Check if user exists
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already taken')
                return render(request, 'registration/signup.html')
            
            # Create user
            user = User.objects.create_user(
                username=username,
                email=email or f'{username}@example.com',
                password=password1
            )
            
            # Login user immediately
            login(request, user)
            messages.success(request, f'Welcome {username}! Account created successfully.')
            return redirect('dashboard')
            
        except Exception as e:
            # Show specific error for debugging
            messages.error(request, f'Account creation failed: {str(e)}')
            return render(request, 'registration/signup.html')
    
    return render(request, 'registration/signup.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '')
        
        if not username or not password:
            messages.error(request, 'Please enter both username and password')
            return render(request, 'registration/login.html')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome back, {user.username}!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password')
            return render(request, 'registration/login.html')
    
    return render(request, 'registration/login.html')

def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully')
    return redirect('login')

@login_required
def dashboard_view(request):
    return render(request, 'dashboard/dashboard.html', {
        'user': request.user
    })