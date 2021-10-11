from django.contrib import admin

from .models import Project


class ProjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug', 'timestamp', 'updated']
    search_fields = ['name', 'type', 'governance']


admin.site.register(Project, ProjectAdmin)
