from django.urls import path
from django.http import HttpResponse

def home_view(request):
    return HttpResponse('<h1>UptimeGuard - Website Monitoring SaaS</h1><p>Professional monitoring service</p><a href="/dashboard/">Go to Dashboard</a>')

def dashboard_view(request):
    return HttpResponse('<h1>Dashboard</h1><p>Welcome to your monitoring dashboard</p><a href="/">Back to Home</a>')

urlpatterns = [
    path('', home_view, name='home'),
    path('dashboard/', dashboard_view, name='dashboard'),
]