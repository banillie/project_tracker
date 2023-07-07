# not in use handled via form_class in engagement.views

from django import forms

from .models import Engagement, EngagementTopic
from projects.models import Project
from stakeholders.models import Stakeholder
from ppdds.models import PPDD
from easy_select2 import select2_modelform_meta, Select2Multiple


class EngagementForm(forms.ModelForm):
    projects = forms.ModelMultipleChoiceField(
        queryset=Project.objects.all(),
        widget=Select2Multiple(
            select2attrs={
                "width": "100%",
                "placeholder": "Type and/or select project from list. If project not in database use create "
                "new project button.",
            }
        ),
    )
    stakeholders = forms.ModelMultipleChoiceField(
        queryset=Stakeholder.objects.all(),
        widget=Select2Multiple(
            select2attrs={
                "width": "100%",
                "placeholder": "Type and/or select stakeholder from list. If stakeholder not in database use create "
                               "new stakeholder button.",
            }
        ),
    )
    ppdds = forms.ModelMultipleChoiceField(
        queryset=PPDD.objects.all(),
        widget=Select2Multiple(
            select2attrs={
                "width": "100%",
                "placeholder": "Type and/or select ppdd colleagues from list. If they are not in database use "
                               "create new ppdd button.",
            }
        ),
        label="PPDD Colleagues",
    )
    topics = forms.ModelMultipleChoiceField(
        queryset=EngagementTopic.objects.all(),
        widget=Select2Multiple(
            select2attrs={
                "width": "100%",
                "placeholder": "Type and/or select topic from list. Please contact admin if new topic type is required."
            }
        ),
        label="Engagement Topics",
    )
    # summary = forms.CharField(
    #     widget=forms.Textarea,
    #     required=False,
    # )

    class Meta:
        model = Engagement
        fields = [
            "date",
            "projects",
            "stakeholders",
            "ppdds",
            "topics",
            "summary",
        ]

        widgets = {
            "date": forms.DateInput(
                # date type expects an input in the format "%Y-%m-%d"
                # but is then converted to local format ??
                format="%Y-%m-%d",
                attrs={"class": "form-control", "type": "date"},
            ),
            "summary": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter a summary of meeting and any outcomes/actions arising from it.",
                },
            ),
        }

    def __init__(self, *args, **kwargs):
        super(EngagementForm, self).__init__(*args, **kwargs)
        # validation
        self.fields["date"].required = True
        self.fields["projects"].required = True
        self.fields["stakeholders"].required = True
        self.fields["ppdds"].required = True
        self.fields["topics"].required = False
        self.fields["summary"].required = True
        # label
        # self.fields["date"].label = "Date of Engagement"
