from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin

from .models import PPDD, PPDDDivison



class PPDDAdmin(SimpleHistoryAdmin):
    # list_display = ['name', 'slug', 'timestamp', 'updated']
    # fields = ['user', 'first_name', 'last_name', 'slug', 'team', 'role']
    list_display = ['full_name', 'division', 'team', 'role']
    ordering = ['first_name', ]
    search_fields = ['first_name', 'last_name', 'team', 'role']

    def full_name(self, obj):
        return obj


admin.site.register(PPDD, PPDDAdmin)
admin.site.register(PPDDDivison, SimpleHistoryAdmin)
