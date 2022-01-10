from django import forms

from .models import PPDD


class PPDDForm(forms.ModelForm):
    # first_name = forms.CharField(max_length=40)
    # last_name = forms.CharField(max_length=40)
    # role = forms.CharField(max_length=100, required=False)
    # tele_no = forms.CharField(max_length=1000, required=False)

    class Meta:
        model = PPDD
        fields = [
            "first_name",
            "last_name",
            "role",
            "tele_no",
        ]
        widgets = {
            "first_name": forms.TextInput(attrs={'class': 'form-control'}),
            "last_name": forms.TextInput(attrs={'class': 'form-control'}),
            "role": forms.TextInput(attrs={'class': 'form-control'}),
            "tele_no": forms.TextInput(attrs={'class': 'form-control'}),
        }