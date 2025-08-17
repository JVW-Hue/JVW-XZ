from django.urls import path
from . import views

urlpatterns = [
    path('', views.public_status_page, name='public_status_page'),
]