from django import forms
from django.forms import Select

from .models import Engagement


class EngagementForm(forms.ModelForm):
    # date = forms.DateField(input_formats=DATE_INPUT_FORMATS)
    date = forms.DateField(widget=forms.DateInput(format='%d/%m/%Y'))

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
