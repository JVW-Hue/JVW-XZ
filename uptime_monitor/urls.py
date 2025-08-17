from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='landing.html'), name='home'),
    path('auth/', include('uptime_monitor.apps.core.urls')),
    path('dashboard/', include('uptime_monitor.apps.monitoring.urls')),
    path('api/', include('uptime_monitor.apps.monitoring.api_urls')),
    path('billing/', include('uptime_monitor.apps.billing.urls')),
    path('status/<str:slug>/', include('uptime_monitor.apps.monitoring.status_urls')),
]