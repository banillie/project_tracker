from django.contrib import admin
from easy_select2 import select2_modelform

from .models import Engagement, EngagementType, EngagementWorkStream, EngagementTopic

from simple_history.admin import SimpleHistoryAdmin


class EngagementAdmin(SimpleHistoryAdmin):
    form = select2_modelform(Engagement)
    # fields = ['date', 'projects', 'stakeholders']
    list_display = ['date', 'get_projects', 'get_stakeholders', 'get_topics']
    ordering = ['-date', ]
    search_fields = [
        'date',
        'projects__name',
        'stakeholders__first_name',
        'stakeholders__last_name',
        'topics__topic'
    ]

    def get_projects(self, obj):
        return ",\n".join([p.name for p in obj.projects.all()])

    def get_stakeholders(self, obj):
        return ",\n".join([str(s) for s in obj.stakeholders.all()])

    def get_topics(self, obj):
        return ",\n".join([t.topic for t in obj.topics.all()])

# class EngagementAdmin(SimpleHistoryAdmin):
#     form = select2_modelform(Engagement)
#     list_display = ['date']


admin.site.register(Engagement, EngagementAdmin)
admin.site.register(EngagementTopic)


"""from .models import Engagement

from django.contrib import admin
from easy_select2 import select2_modelform

# admin.site.register(Engagement)
# admin.site.register(EngagementProjects)

PollForm = select2_modelform(Engagement, attrs={'width': '250px'})


class PollAdmin(admin.ModelAdmin):
    form = PollForm"""
