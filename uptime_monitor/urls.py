from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

def home_redirect(request):
    if request.user.is_authenticated:
        return redirect('/dashboard/')
    return redirect('/auth/login/')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_redirect, name='home'),
    path('auth/', include('core.urls')),
    path('dashboard/', include('monitoring.urls')),
    path('billing/', include('billing.urls')),
]