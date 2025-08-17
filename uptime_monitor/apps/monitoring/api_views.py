from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .models import Website, Check

class WebsiteListAPI(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        websites = request.user.websites.all()
        data = []
        
        for website in websites:
            recent_check = website.checks.first()
            data.append({
                'id': website.id,
                'name': website.name,
                'url': website.url,
                'is_up': recent_check.is_up if recent_check else True,
                'uptime_30d': website.get_uptime_percentage(30),
                'last_check': recent_check.checked_at.isoformat() if recent_check else None,
            })
        
        return Response(data)

class WebsiteChecksAPI(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, website_id):
        website = get_object_or_404(Website, id=website_id, user=request.user)
        checks = website.checks.all()[:100]
        
        data = [{
            'checked_at': check.checked_at.isoformat(),
            'is_up': check.is_up,
            'response_time': check.response_time,
            'status_code': check.status_code,
        } for check in checks]
        
        return Response(data)