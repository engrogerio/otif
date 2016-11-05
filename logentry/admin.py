from django.contrib.admin.models import LogEntry
from django.contrib import admin

class LogEntryAdmin(admin.ModelAdmin):

    def has_change_permission(self, request, obj=None):
        return True
    def has_add_permission(self, request, obj=None):
        return False

    """Create an admin view of the history/log table"""
    list_display = ('action_time','user','content_type','change_message','is_addition','is_change','is_deletion','object_repr')
    list_filter = ['action_time','user','content_type']
    ordering = ('-action_time',)

#Just the list not details
    def __init__(self, *args, **kwargs):
        super(LogEntryAdmin, self).__init__(*args, **kwargs)
        self.list_display_links = (None, )

admin.site.register(LogEntry, LogEntryAdmin,)