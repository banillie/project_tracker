from django import forms

from .models import PPDD


class PPDDForm(forms.ModelForm):
    class Meta:
        model = PPDD
        fields = [
            "first_name",
            "last_name",
            "division",
            "role",
            "tele_no",
        ]
        widgets = {
            "first_name": forms.TextInput(attrs={'class': 'form-control'}),
            "last_name": forms.TextInput(attrs={'class': 'form-control'}),
            "division": forms.Select(attrs={'class': 'form-control'}),
            "role": forms.TextInput(attrs={'class': 'form-control'}),
            "tele_no": forms.TextInput(attrs={'class': 'form-control'}),
        }


    def __init__(self, *args, **kwargs):
        super(PPDDForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].label = "First Name"
        self.fields['last_name'].label = "Last Name"
        self.fields['tele_no'].label = "Telephone Number"
        # self.fields['scope'].label = "Brief Outline Of Scope"
        # validation
        # self.fields['name'].required = True
