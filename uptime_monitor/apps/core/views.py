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
        
        # Validation
        if not username:
            messages.error(request, 'Username is required')
            return render(request, 'registration/signup.html')
            
        if len(username) < 3:
            messages.error(request, 'Username must be at least 3 characters')
            return render(request, 'registration/signup.html')
            
        if not password1:
            messages.error(request, 'Password is required')
            return render(request, 'registration/signup.html')
            
        if len(password1) < 6:
            messages.error(request, 'Password must be at least 6 characters')
            return render(request, 'registration/signup.html')
            
        if password1 != password2:
            messages.error(request, 'Passwords do not match')
            return render(request, 'registration/signup.html')
        
        try:
            # Create user
            user = User.objects.create_user(
                username=username,
                password=password1,
                email=f'{username}@example.com'
            )
            
            # Login user immediately
            user = authenticate(username=username, password=password1)
            if user:
                login(request, user)
                messages.success(request, 'Account created successfully!')
                return redirect('dashboard')
            else:
                messages.error(request, 'Account created but login failed')
                return redirect('login')
                
        except IntegrityError:
            messages.error(request, 'Username already exists')
            return render(request, 'registration/signup.html')
        except Exception as e:
            messages.error(request, 'Error creating account. Please try again.')
            return render(request, 'registration/signup.html')
    
    return render(request, 'registration/signup.html')