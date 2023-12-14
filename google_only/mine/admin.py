from django.contrib import admin
from .models import UserProfile

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'fun_number')
    search_fields = ('user__username', 'user__email')  # Enable searching by username or email
    list_filter = ('fun_number',)  # Enable filtering by fun_number
