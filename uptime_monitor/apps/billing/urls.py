from django.urls import path
from . import views

urlpatterns = [
    path('pricing/', views.pricing, name='pricing'),
    path('checkout/<str:plan>/', views.create_checkout_session, name='create_checkout_session'),
    path('paypal/<str:plan>/', views.paypal_checkout, name='paypal_checkout'),
    path('paypal-success/', views.paypal_success, name='paypal_success'),
    path('paypal-success-page/', views.paypal_success_page, name='paypal_success_page'),
    path('success/', views.success, name='billing_success'),
    path('webhook/', views.stripe_webhook, name='stripe_webhook'),
]