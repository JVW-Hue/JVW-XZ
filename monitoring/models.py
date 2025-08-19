from django.db import models
from django.contrib.auth.models import User

class Website(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='websites')
    name = models.CharField(max_length=200)
    url = models.URLField()
    check_interval = models.IntegerField(default=300)  # seconds
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name} - {self.url}"
    
    def get_latest_check(self):
        return self.uptime_checks.first()
    
    def get_uptime_percentage(self):
        total_checks = self.uptime_checks.count()
        if total_checks == 0:
            return 100
        online_checks = self.uptime_checks.filter(is_online=True).count()
        return round((online_checks / total_checks) * 100, 1)

class UptimeCheck(models.Model):
    website = models.ForeignKey(Website, on_delete=models.CASCADE, related_name='uptime_checks')
    is_online = models.BooleanField()
    response_time = models.FloatField()  # milliseconds
    status_code = models.IntegerField()
    error_message = models.TextField(blank=True, null=True)
    checked_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-checked_at']
    
    def __str__(self):
        status = "Online" if self.is_online else "Offline"
        return f"{self.website.name} - {status} at {self.checked_at}"