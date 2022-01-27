from django.contrib import admin

from .models import Project, Tier


class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'timestamp', 'updated']
    search_fields = ['name', 'type', 'governance']
    # raw_id_fields =


admin.site.register(Project, ProjectAdmin)

admin.site.register(Tier)


