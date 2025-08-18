from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    PLAN_CHOICES = [
        ('free', 'Free'),
        ('premium', 'Premium'),
        ('pro', 'Pro'),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    plan = models.CharField(max_length=10, choices=PLAN_CHOICES, default='free')
    stripe_customer_id = models.CharField(max_length=100, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def get_monitor_limit(self):
        limits = {'free': 1, 'premium': 5, 'pro': 999}
        return limits.get(self.plan, 1)
    
    def can_use_sms(self):
        return self.plan == 'pro'
    
    def can_use_status_page(self):
        return self.plan == 'pro'