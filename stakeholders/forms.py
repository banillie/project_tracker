from django import forms

from .models import Stakeholder, DFTGroup


class StakeholderForm(forms.ModelForm):

    class Meta:
        model = Stakeholder
        fields = [
            "first_name",
            "last_name",
            "organisation",
            "group",
            "dft_group",
            "team",
            "role",
            "tele_no",
            "my_dft_url"
        ]

        widgets = {
            "first_name": forms.TextInput(attrs={'class': 'form-control'}),
            "last_name": forms.TextInput(attrs={'class': 'form-control'}),
            "organisation": forms.Select(attrs={'class': 'form-control'}),
            "group": forms.TextInput(attrs={'class': 'form-control'}),
            "dft_group": forms.Select(attrs={'class': 'form-control'}),
            "team": forms.TextInput(attrs={'class': 'form-control'}),
            "role": forms.TextInput(attrs={'class': 'form-control'}),
            "tele_no": forms.TextInput(attrs={'class': 'form-control'}),
            "my_dft_url": forms.URLInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(StakeholderForm, self).__init__(*args, **kwargs)
        self.fields['my_dft_url'].label = "MyDfT Contact Link (automatically created if left blank)"


