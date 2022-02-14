from django.contrib import admin
from .models import Project, Tier
from simple_history.admin import SimpleHistoryAdmin


class ProjectAdmin(SimpleHistoryAdmin):
    # list_display = ['name', 'slug', 'timestamp', 'updated']
    list_display = ['name', 'updated']
    search_fields = ['name', 'type', 'governance']


admin.site.register(Project, ProjectAdmin)

admin.site.register(Tier, SimpleHistoryAdmin)


