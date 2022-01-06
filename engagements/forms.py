# not in use handled via form_class in engagement.views

from django import forms

from .models import Engagement
from easy_select2 import select2_modelform_meta

#
# class EngagementForm(forms.ModelForm):
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