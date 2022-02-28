from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin

from .models import Stakeholder, StakeholderOrg, DFTGroup

admin.site.register(Stakeholder, SimpleHistoryAdmin)
admin.site.register(StakeholderOrg, SimpleHistoryAdmin)
admin.site.register(DFTGroup, SimpleHistoryAdmin)