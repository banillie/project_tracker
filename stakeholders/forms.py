from django import forms

from .models import Stakeholder


class StakeholderForm(forms.ModelForm):
    # first_name = forms.CharField(max_length=40)
    # last_name = forms.CharField(max_length=40)
    # organisation = forms.CharField(max_length=60)
    # group = forms.CharField(max_length=100)
    # team = forms.CharField(max_length=100, required=False)
    # role = forms.CharField(max_length=100, required=False)
    # tele_no = forms.CharField(max_length=1000, required=False)

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
        ]

        widgets = {
            "first_name": forms.TextInput(attrs={'class': 'form-control'}),
            "last_name": forms.TextInput(attrs={'class': 'form-control'}),
            "organisation": forms.Select(attrs={'class': 'form-control'}),
            "group": forms.TextInput(attrs={'class': 'form-control'}),
            "team": forms.TextInput(attrs={'class': 'form-control'}),
            "role": forms.TextInput(attrs={'class': 'form-control'}),
            "tele_no": forms.TextInput(attrs={'class': 'form-control'}),
        }


