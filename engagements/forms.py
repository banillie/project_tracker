from django import forms

from .models import Engagement, ProjectEngagement


class EngagementForm(forms.ModelForm):
    # date = forms.DateField()
    # summary = forms.TextInput()
    # follow_up_date = forms.DateField()

    class Meta:
        model = Engagement
        fields = [
            "date",
            "project",
            "stakeholder",
            "ppdd",
            "type",
            "ws_type",
            "summary",
            "follow_up_date",
        ]



class ProjectEngagementForm(forms.ModelForm):
    class Meta:
        model = ProjectEngagement
        exclude = ('projects',)