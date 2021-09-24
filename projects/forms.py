from django import forms

from .models import Project


class ProjectForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Project Name"})
    )
    # type = forms.CharField()
    abbreviation = forms.CharField()
    governance = forms.CharField(required=False)
    stage = forms.CharField(required=False)
    scope = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                "rows": 10,
                "cols": 100,
            }
        ),
    )

    class Meta:
        model = Project
        fields = [
            "name",
            "type",
            "abbreviation",
            "governance",
            "stage",
            "scope",
            # "live",
        ]

    # # for adding data validation requirements
    # # could be useful for email / tele numbers
    # def clean_name(self, *args, **kwargs):
    #     name = self.cleaned_data.get("name")
    #     if not "Project" in name:
    #         raise forms.ValidationError("This is not a v project name")


class RawProjectForm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Project Name"})
    )
    type = forms.CharField()
    abbreviation = forms.CharField()
    governance = forms.CharField(required=False)
    stage = forms.CharField(required=False)
    scope = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                "rows": 10,
                "cols": 100,
            }
        ),
    )
