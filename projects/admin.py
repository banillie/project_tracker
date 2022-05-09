from django.contrib import admin
from .models import Project, Tier, Stage
from simple_history.admin import SimpleHistoryAdmin


class ProjectAdmin(SimpleHistoryAdmin):
    # list_display = ['name', 'slug', 'timestamp', 'updated']
    fields = ['user', 'name', 'slug', 'abbreviation', 'type', 'tier', 'dft_group', 'stage_name']
    list_display = ['name', 'abbreviation', 'type', 'tier', 'dft_group']
    ordering = ['name', ]
    search_fields = ['name', 'type', 'tier__type', 'abbreviation', 'dft_group__name']


admin.site.register(Project, ProjectAdmin)
admin.site.register(Tier, SimpleHistoryAdmin)
admin.site.register(Stage, SimpleHistoryAdmin)


