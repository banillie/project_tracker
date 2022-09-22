from django.contrib import admin
from .models import Project, Tier, Stage, Type
from simple_history.admin import SimpleHistoryAdmin


class ProjectAdmin(SimpleHistoryAdmin):
    # list_display = ['name', 'slug', 'timestamp', 'updated']
    fields = ['user', 'name', 'slug', 'abbreviation', 'sort', 'tier', 'dft_group', 'stage_name']
    list_display = ['name', 'abbreviation', 'sort', 'tier', 'dft_group']
    ordering = ['name', ]
    search_fields = ['name', 'sort__name', 'tier__type', 'abbreviation', 'dft_group__name']


admin.site.register(Project, ProjectAdmin)
admin.site.register(Tier, SimpleHistoryAdmin)
admin.site.register(Stage, SimpleHistoryAdmin)
admin.site.register(Type, SimpleHistoryAdmin)

