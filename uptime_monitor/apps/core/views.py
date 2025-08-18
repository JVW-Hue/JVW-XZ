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
        
        # Validation
        if not username or not password1 or not password2:
            messages.error(request, 'All fields are required')
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
        
        # Check if user already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
            return render(request, 'registration/signup.html')
            
        if email and User.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered')
            return render(request, 'registration/signup.html')
        
        try:
            # Create user
            user = User.objects.create_user(
                username=username,
                email=email or f'{username}@example.com',
                password=password1
            )
            
            # Auto login after signup
            user = authenticate(username=username, password=password1)
            if user:
                login(request, user)
                messages.success(request, 'Account created successfully! Welcome!')
                return redirect('dashboard')
            else:
                messages.success(request, 'Account created! Please log in.')
                return redirect('login')
                
        except IntegrityError:
            messages.error(request, 'Username or email already exists')
            return render(request, 'registration/signup.html')
        except Exception as e:
            messages.error(request, 'Error creating account. Please try again.')
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