from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render, redirect
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse
from django.views.generic import RedirectView

def home_view(request):
    if request.user.is_authenticated:
        return redirect('/dashboard/')
    return render(request, 'landing.html')

def handler404(request, exception):
    return render(request, '404.html', status=404)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('auth/', include('core.urls')),
    path('dashboard/', include('monitoring.urls')),
    path('billing/', include('billing.urls')),
    path('favicon.ico', RedirectView.as_view(url='/static/favicon.ico')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler404 = 'uptime_monitor.urls.handler404'