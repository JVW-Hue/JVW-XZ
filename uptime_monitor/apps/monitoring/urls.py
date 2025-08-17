from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('add/', views.add_website, name='add_website'),
    path('website/<int:website_id>/', views.website_detail, name='website_detail'),
    path('website/<int:website_id>/delete/', views.delete_website, name='delete_website'),
    path('status-page/', views.manage_status_page, name='manage_status_page'),
]