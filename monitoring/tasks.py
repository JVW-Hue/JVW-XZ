import requests
from datetime import datetime
from .models import Website, UptimeCheck

def check_website_status(website):
    """Check if a website is online and record the result"""
    try:
        response = requests.get(website.url, timeout=10)
        is_online = response.status_code == 200
        response_time = response.elapsed.total_seconds() * 1000  # Convert to milliseconds
        
        # Create uptime check record
        UptimeCheck.objects.create(
            website=website,
            is_online=is_online,
            response_time=response_time,
            status_code=response.status_code
        )
        
        return {
            'is_online': is_online,
            'response_time': response_time,
            'status_code': response.status_code
        }
    except Exception as e:
        # Website is down
        UptimeCheck.objects.create(
            website=website,
            is_online=False,
            response_time=0,
            status_code=0,
            error_message=str(e)
        )
        
        return {
            'is_online': False,
            'response_time': 0,
            'status_code': 0,
            'error': str(e)
        }