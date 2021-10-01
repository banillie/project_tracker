from django.contrib import admin
from easy_select2 import select2_modelform

from .models import Engagement


class NoteAdmin(admin.ModelAdmin):
    form = select2_modelform(Engagement)


admin.site.register(Engagement)



"""from .models import Engagement

from django.contrib import admin
from easy_select2 import select2_modelform

# admin.site.register(Engagement)
# admin.site.register(EngagementProjects)

PollForm = select2_modelform(Engagement, attrs={'width': '250px'})


class PollAdmin(admin.ModelAdmin):
    form = PollForm"""
