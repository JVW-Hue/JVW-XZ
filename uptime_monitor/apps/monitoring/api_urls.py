from django.urls import path
from . import api_views

urlpatterns = [
    path('websites/', api_views.WebsiteListAPI.as_view(), name='api_websites'),
    path('websites/<int:website_id>/checks/', api_views.WebsiteChecksAPI.as_view(), name='api_website_checks'),
]