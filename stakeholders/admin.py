from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin

from .models import Stakeholder, StakeholderOrg, DFTGroup

class StakeholderAdmin(SimpleHistoryAdmin):
    # list_display = ['name', 'slug', 'timestamp', 'updated']
    fields = ['user', 'first_name', 'last_name', 'slug', 'organisation', 'dft_group', 'team', 'role']
    list_display = ['full_name', 'organisation', 'dft_group', 'team']
    ordering = ['last_name', ]
    search_fields = ['first_name', 'last_name', 'organisation__name', 'dft_group__name', 'team']

    def full_name(self, obj):
        return obj


admin.site.register(Stakeholder, StakeholderAdmin)
admin.site.register(StakeholderOrg, SimpleHistoryAdmin)
admin.site.register(DFTGroup, SimpleHistoryAdmin)