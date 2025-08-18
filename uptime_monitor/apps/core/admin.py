from django.contrib import admin
from django.contrib.auth.models import User
from .models import UserProfile

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'plan', 'created_at')
    list_filter = ('plan', 'created_at')
    search_fields = ('user__username', 'user__email')
    
    def get_queryset(self, request):
        return super().get_queryset(request).select_related('user')