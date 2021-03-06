from django import forms

from .models import Project, Stage


class ProjectForm(forms.ModelForm):
    # name = forms.CharField(widget=forms.Textarea(attrs={'cols': 50, 'rows': 1}))
    # scope = forms.CharField(required=False, widget=forms.Textarea(attrs={'cols': 50, 'rows': 20}))

    class Meta:
        model = Project
        fields = [
            "name",
            "type",
            "abbreviation",
            "tier",
            "stage_name",
            "scope",
            "dft_group"
        ]
        # filter = ["name", "type"]
        widgets = {
            "name": forms.TextInput(attrs={'class': 'form-control'}),
            "type": forms.Select(attrs={'class': 'form-control'}),
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


    # # for adding data validation requirements
    # def clean(self, *args, **kwargs):
    #     data = self.cleaned_data
    #     name = data.get("name")
    #     qs = Project.objects.filter(name__icontains=name)
    #     if qs.exists():  # this is not right.
    #         self.add_error("name", f"{name} already exists in the database")
    #         # raise forms.ValidationError("This project already exists")
    #     return data

