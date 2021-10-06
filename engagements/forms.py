from django import forms


from .models import Engagement


class EngagementForm(forms.ModelForm):

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
        widgets = {
            'summary': forms.Textarea(attrs={'rows': 4, 'cols': 30}),
        }  # not working. leaving for now as text area can be easily manually altered.
