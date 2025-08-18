from django.urls import path
from . import views

urlpatterns = [
    path('pricing/', views.pricing, name='pricing'),
    path('paypal/<str:plan>/', views.paypal_checkout, name='paypal_checkout'),
    path('paypal-success/', views.paypal_success, name='paypal_success'),
    path('paypal-success-page/', views.paypal_success_page, name='paypal_success_page'),
]