from django.core.management.base import BaseCommand
from uptime_monitor.apps.monitoring.models import Website
import requests
import time

class Command(BaseCommand):
    help = 'Check all websites manually'

    def handle(self, *args, **options):
        websites = Website.objects.filter(is_active=True)
        for website in websites:
            self.check_website(website)
        self.stdout.write(self.style.SUCCESS(f'Successfully checked {websites.count()} websites'))
    
    def check_website(self, website):
        from uptime_monitor.apps.monitoring.models import Check
        
        start_time = time.time()
        is_up = False
        status_code = None
        error_message = ""
        
        try:
            response = requests.get(website.url, timeout=30)
            response_time = (time.time() - start_time) * 1000
            status_code = response.status_code
            is_up = 200 <= status_code < 400
        except requests.exceptions.RequestException as e:
            response_time = (time.time() - start_time) * 1000
            error_message = str(e)
            is_up = False
        
        Check.objects.create(
            website=website,
            is_up=is_up,
            response_time=response_time,
            status_code=status_code,
            error_message=error_message
        )
        
        self.stdout.write(f'Checked {website.name}: {"UP" if is_up else "DOWN"} ({response_time:.0f}ms)')