from django.contrib import admin
from easy_select2 import select2_modelform

from .models import Engagement, EngagementType, EngagementWorkStream, EngagementTopic


class EngagementAdmin(admin.ModelAdmin):
    form = select2_modelform(Engagement)

# class EngagementTopicAdmin(admin.ModelAdmin):
#    """ Team Role admin view with modifications """
#    model = EngagementTopic
#    ordering = ['topic']


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
