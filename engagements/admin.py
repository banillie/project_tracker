from django.contrib import admin
from easy_select2 import select2_modelform

from .models import Engagement, EngagementType, EngagementWorkStream


class EngagementAdmin(admin.ModelAdmin):
    form = select2_modelform(Engagement)


admin.site.register(Engagement, EngagementAdmin)
admin.site.register(EngagementType)
admin.site.register(EngagementWorkStream)


"""from .models import Engagement

from django.contrib import admin
from easy_select2 import select2_modelform

# admin.site.register(Engagement)
# admin.site.register(EngagementProjects)

PollForm = select2_modelform(Engagement, attrs={'width': '250px'})


class PollAdmin(admin.ModelAdmin):
    form = PollForm"""
