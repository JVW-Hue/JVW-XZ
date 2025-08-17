from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from .models import User

def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        
        if password1 != password2:
            messages.error(request, 'Passwords do not match')
            return render(request, 'registration/signup.html')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
            return render(request, 'registration/signup.html')
        
        try:
            user = User.objects.create_user(username=username, password=password1)
            login(request, user)
            messages.success(request, 'Account created successfully!')
            return redirect('dashboard')
        except Exception as e:
            messages.error(request, 'Error creating account')
            return render(request, 'registration/signup.html')
    
    return render(request, 'registration/signup.html')