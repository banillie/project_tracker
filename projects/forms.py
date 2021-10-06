from django import forms

from .models import Project


class ProjectForm(forms.ModelForm):
    name = forms.CharField(widget=forms.Textarea(attrs={'cols': 50, 'rows': 1}))
    scope = forms.CharField(required=False, widget=forms.Textarea(attrs={'cols': 50, 'rows': 20}))

    class Meta:
        model = Project
        fields = [
            "name",
            "type",
            "abbreviation",
            "governance",
            "stage",
            "scope",
        ]

    # # for adding data validation requirements
    # # could be useful for email / tele numbers
    # def clean_name(self, *args, **kwargs):
    #     name = self.cleaned_data.get("name")
    #     if not "Project" in name:
    #         raise forms.ValidationError("This is not a v project name")

