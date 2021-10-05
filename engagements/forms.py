from django import forms
from django.forms import Select
from easy_select2 import Select2


from .models import Engagement


class EngagementForm(forms.ModelForm):
    # projects = Select2(select2attrs={'width': '1000px'})
    projects = forms.CharField(widget=forms.TextInput(attrs={'cols': 500}))

    class Meta:
        model = Engagement
        fields = [
            "date",
            "projects",
            "stakeholders",
            "ppdds",
            "engagement_types",
            "engagement_workstreams",
            "summary",
            "follow_up_date",
        ]
        Select2.widgets = {
            # 'cols': '400',
            'width': '1000px',
        }
