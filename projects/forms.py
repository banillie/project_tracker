from django import forms

from .models import Project, Stage


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = [
            "name",
            "sort",
            "abbreviation",
            "dft_group",
            "tier",
            "stage_name",
            "scope",
        ]
        widgets = {
            "name": forms.TextInput(attrs={'class': 'form-control'}),
            "sort": forms.Select(attrs={'class': 'form-control'}),
            "dft_group": forms.Select(attrs={'class': 'form-control'}),
            "abbreviation": forms.TextInput(attrs={'class': 'form-control'}),
            "tier": forms.Select(attrs={'class': 'form-control'}),
            "stage_name": forms.Select(attrs={'class': 'form-control'}),
            "scope": forms.Textarea(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        self.fields['stage_name'].label = "Business Case Stage"
        self.fields['dft_group'].label = "DfT Group"
        self.fields['scope'].label = "Brief Outline Of Scope"
        # validation
        self.fields['name'].required = True
        self.fields['sort'].required = True
        self.fields['abbreviation'].required = True
        self.fields['dft_group'].required = True
        self.fields['tier'].required = False
        self.fields['stage_name'].required = False
        self.fields['scope'].required = True

    # # for adding data validation requirements
    # def clean(self, *args, **kwargs):
    #     data = self.cleaned_data
    #     name = data.get("name")
    #     qs = Project.objects.filter(name__icontains=name)
    #     if qs.exists():  # this is not right.
    #         self.add_error("name", f"{name} already exists in the database")
    #         # raise forms.ValidationError("This project already exists")
    #     return data

