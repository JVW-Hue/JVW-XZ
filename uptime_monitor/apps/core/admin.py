from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'plan', 'created_at', 'is_active')
    list_filter = ('plan', 'is_active', 'created_at')
    search_fields = ('username', 'email')
    
    fieldsets = UserAdmin.fieldsets + (
        ('Subscription', {'fields': ('plan', 'stripe_customer_id', 'phone_number')}),
    )