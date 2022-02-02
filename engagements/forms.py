# not in use handled via form_class in engagement.views

from django import forms

from .models import Engagement, EngagementType, EngagementWorkStream
from projects.models import Project
from stakeholders.models import Stakeholder
from ppdds.models import PPDD
from easy_select2 import select2_modelform_meta, Select2Multiple


class EngagementForm(forms.ModelForm):
    date = forms.DateTimeField(input_formats=['%d/%m/%Y'])
    projects = forms.ModelMultipleChoiceField(
        queryset=Project.objects.all(),
        widget=Select2Multiple(select2attrs={'width': '100%'})
    )
    stakeholders = forms.ModelMultipleChoiceField(
        queryset=Stakeholder.objects.all(),
        widget=Select2Multiple(select2attrs={'width': '100%'})
    )
    ppdds = forms.ModelMultipleChoiceField(
        queryset=PPDD.objects.all(),
        widget=Select2Multiple(select2attrs={'width': '100%'}),
        label='PPDD colleagues'
    )
    engagement_types = forms.ModelMultipleChoiceField(
        queryset=EngagementType.objects.all(),
        widget=Select2Multiple(select2attrs={'width': '100%'}),
        label='Engagement Topic'
    )
    engagement_workstreams = forms.ModelMultipleChoiceField(
        queryset=EngagementWorkStream.objects.all(),
        widget=Select2Multiple(select2attrs={'width': '100%'}),
    )
    summary = forms.CharField(
        widget=forms.Textarea,
        required=False,
    )

    class Meta:
        model = Engagement
        fields = [
            'date',
            'projects',
            'stakeholders',
            'ppdds',
            'engagement_types',
            'engagement_workstreams',
            'summary',
        ]

