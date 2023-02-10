from django import forms

from .models import Project, Stage


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = [
            "name",
            "sort",
            "abbreviation",
            "tier",
            "stage_name",
            "scope",
            "dft_group"
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
        # self.fields['abbreviation'].label = "Project Abbreviation"
        self.fields['dft_group'].label = "DfT Group"
        # self.fields['sort'].label = "Type"

    # # for adding data validation requirements
    # def clean(self, *args, **kwargs):
    #     data = self.cleaned_data
    #     name = data.get("name")
    #     qs = Project.objects.filter(name__icontains=name)
    #     if qs.exists():  # this is not right.
    #         self.add_error("name", f"{name} already exists in the database")
    #         # raise forms.ValidationError("This project already exists")
    #     return data

