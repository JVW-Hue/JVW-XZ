from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('add/', views.add_website, name='add_website'),
    path('website/<int:website_id>/', views.website_detail, name='website_detail'),
]