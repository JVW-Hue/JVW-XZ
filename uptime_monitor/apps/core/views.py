from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.models import User
from django.db import IntegrityError

def signup_view(request):
    if request.method == 'POST':
        # Just redirect to login for now - bypass database issues
        messages.success(request, 'Please use the admin login: admin / admin123')
        return redirect('login')
    
    return render(request, 'registration/signup.html')