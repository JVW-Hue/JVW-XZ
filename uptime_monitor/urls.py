from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render, redirect

def home_view(request):
    if request.user.is_authenticated:
        return redirect('/dashboard/')
    return render(request, 'landing.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('auth/', include('core.urls')),
    path('dashboard/', include('monitoring.urls')),
    path('billing/', include('billing.urls')),
]