from django import forms
from django.forms import Select

from .models import Engagement
from projects.models import Project


class EngagementForm(forms.ModelForm):
    # date = forms.DateField()
    # summary = forms.TextInput()
    # follow_up_date = forms.DateField()
    # projects = forms.CharField(max_length=120, widget={})
    # projects = forms.ModelMultipleChoiceField(queryset=Project.objects.all())
    # projects = forms.ModelChoiceField(queryset=Project.objects.all())

    class Meta:
        model = Engagement
        fields = [
            "date",
            "projects",
            "stakeholders",
            "ppdds",
            "type",
            "ws_type",
            "summary",
            "follow_up_date",
        ]


# class ProjectEngagementForm(forms.ModelForm):
#     class Meta:
#         model = ProjectEngagement
#         exclude = ('projects',)