from django.contrib import admin
from .models import Project, Tier, Stage
from simple_history.admin import SimpleHistoryAdmin


class ProjectAdmin(SimpleHistoryAdmin):
    # list_display = ['name', 'slug', 'timestamp', 'updated']
    list_display = ['name', 'tier', 'dft_group', 'updated']
    search_fields = ['name', 'type', 'tier__type', ]


admin.site.register(Project, ProjectAdmin)
admin.site.register(Tier, SimpleHistoryAdmin)
admin.site.register(Stage, SimpleHistoryAdmin)


