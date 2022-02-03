from django.contrib import admin

from .models import Project, Tier


class ProjectAdmin(admin.ModelAdmin):
    # list_display = ['name', 'slug', 'timestamp', 'updated']
    list_display = ['name', 'updated']
    search_fields = ['name', 'type', 'governance']


admin.site.register(Project, ProjectAdmin)

admin.site.register(Tier)


