# not in use handled via form_class in engagement.views

from django import forms

from .models import Engagement
from projects.models import Project
from easy_select2 import select2_modelform_meta, Select2Multiple
from easy_select2 import select2_modelform


class EngagementForm(forms.Form):
    date = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'])
    # projects = forms.ModelMultipleChoiceField(queryset=Project.objects.all(), widget=Select2Multiple(
    #     select2attrs={'width': '100%'}
    # ))
    # projects = forms.ModelMultipleChoiceField(queryset=Project.objects.all())

    class Meta:
        model = Engagement
        fields = [
            'date',
            'projects',
        ]

        # widgets = {
        #     'projects': Select2Multiple(select2attrs={'width': '100%'})
        # }

    # Engagement.objects.all().order_by('-date')

# class EngagementForm(forms.ModelForm):
#     date = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'])
#     # Meta = select2_modelform_meta(Engagement, attrs={'width': '100%'})
#
#     class Meta:
#         model = Engagement
#         fields = [
#             "date",
#             "projects",
#             "stakeholders",
#             "ppdds",
#             "engagement_types",
#             "engagement_workstreams",
#             "summary",
#             "follow_up_date",
#         ]
#         widgets = {
#             'projects': select2_modelform(select, attrs={'width': '100%'})
#         }
#
#         # widgets = {
#         #     'summary': forms.Textarea(attrs={'rows': 4, 'cols': 30}),
#         # }  # not working. leaving for now as text area can be easily manually altered.
#         # raw_id_field = ["projects"]  # does nothing leaving for now in case useful
#

# class EngagementForm(forms.ModelForm):
#     date = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'])
#
#     class Meta:
#         model = select2_modelform(Engagement, attrs={'width': '100%'})
#         fields = [
#             "date",
#             "projects",
#             "stakeholders",
#             "ppdds",
#             "engagement_types",
#             "engagement_workstreams",
#             "summary",
#             "follow_up_date",
#         ]
#         widgets = {
#             'projects': apply_select2(forms.Select, select2attrs={
#                 'width': '300'}
#             ),
#         }
#
#         # widgets = {
#         #     'summary': forms.Textarea(attrs={'rows': 4, 'cols': 30}),
#         # }  # not working. leaving for now as text area can be easily manually altered.
#         # raw_id_field = ["projects"]  # does nothing leaving for now in case useful


# class EngagementForm(forms.ModelForm):
#     Meta = select2_modelform_meta(Engagement)


class DateForm(forms.Form):
    date = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'])