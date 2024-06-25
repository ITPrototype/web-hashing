from django.contrib import admin
from .models import UserAccessLog

@admin.register(UserAccessLog)
class UserAccessLogAdmin(admin.ModelAdmin):
    list_display = ('ip_address', 'access_time')
    list_filter = ('ip_address',)
    search_fields = ('ip_address',)

