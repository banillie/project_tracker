from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin

from .models import Stakeholder, StakeholderOrg

admin.site.register(Stakeholder, SimpleHistoryAdmin)
admin.site.register(StakeholderOrg, SimpleHistoryAdmin)