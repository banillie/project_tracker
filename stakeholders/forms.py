from django import forms

from .models import Stakeholder


class StakeholderForm(forms.ModelForm):
    class Meta:
        model = Stakeholder
        fields = [
            "first_name",
            "last_name",
            "organisation",
            "group",
            "team",
            "role",
            "tele_no",
            "live",
        ]
