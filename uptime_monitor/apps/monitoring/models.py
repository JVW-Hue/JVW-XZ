from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
import uuid

User = get_user_model()

class Website(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='websites')
    name = models.CharField(max_length=200)
    url = models.URLField()
    check_interval = models.IntegerField(default=300)  # seconds
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name} - {self.url}"
    
    def get_uptime_percentage(self, days=30):
        from django.utils import timezone
        from datetime import timedelta
        
        end_date = timezone.now()
        start_date = end_date - timedelta(days=days)
        
        checks = self.checks.filter(checked_at__range=[start_date, end_date])
        if not checks.exists():
            return 100.0
            
        total_checks = checks.count()
        successful_checks = checks.filter(is_up=True).count()
        return (successful_checks / total_checks) * 100

class Check(models.Model):
    website = models.ForeignKey(Website, on_delete=models.CASCADE, related_name='checks')
    is_up = models.BooleanField()
    response_time = models.FloatField(null=True, blank=True)  # milliseconds
    status_code = models.IntegerField(null=True, blank=True)
    error_message = models.TextField(blank=True)
    checked_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-checked_at']

class Incident(models.Model):
    website = models.ForeignKey(Website, on_delete=models.CASCADE, related_name='incidents')
    started_at = models.DateTimeField()
    ended_at = models.DateTimeField(null=True, blank=True)
    is_resolved = models.BooleanField(default=False)
    
    @property
    def duration(self):
        if self.ended_at:
            return self.ended_at - self.started_at
        return timezone.now() - self.started_at

class StatusPage(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    is_public = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title