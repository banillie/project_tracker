from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin

from .models import PPDD

admin.site.register(PPDD, SimpleHistoryAdmin)
