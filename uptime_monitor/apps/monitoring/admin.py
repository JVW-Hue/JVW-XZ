from django.contrib import admin
from .models import Website, Check, Incident, StatusPage

@admin.register(Website)
class WebsiteAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'user', 'is_active', 'created_at')
    list_filter = ('is_active', 'created_at')
    search_fields = ('name', 'url', 'user__username')

@admin.register(Check)
class CheckAdmin(admin.ModelAdmin):
    list_display = ('website', 'is_up', 'response_time', 'status_code', 'checked_at')
    list_filter = ('is_up', 'checked_at')
    search_fields = ('website__name', 'website__url')

@admin.register(Incident)
class IncidentAdmin(admin.ModelAdmin):
    list_display = ('website', 'started_at', 'ended_at', 'is_resolved')
    list_filter = ('is_resolved', 'started_at')
    search_fields = ('website__name',)

@admin.register(StatusPage)
class StatusPageAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'user', 'is_public', 'created_at')
    list_filter = ('is_public', 'created_at')
    search_fields = ('title', 'slug', 'user__username')