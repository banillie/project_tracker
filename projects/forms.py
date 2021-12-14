from django import forms

from .models import Project


class ProjectForm(forms.ModelForm):
    # name = forms.CharField(widget=forms.Textarea(attrs={'cols': 50, 'rows': 1}))
    # scope = forms.CharField(required=False, widget=forms.Textarea(attrs={'cols': 50, 'rows': 20}))

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
        # filter = ["name", "type"]
        widgets = {
            "name": forms.TextInput(attrs={'class': 'form-control'}),
            "type": forms.Select(attrs={'class': 'form-control'}),
            "abbreviation": forms.TextInput(attrs={'class': 'form-control'}),
            "governance": forms.TextInput(attrs={'class': 'form-control'}),
            "stage": forms.TextInput(attrs={'class': 'form-control'}),
            "scope": forms.Textarea(attrs={'class': 'form-control'}),
        }

    # # for adding data validation requirements
    # def clean(self, *args, **kwargs):
    #     data = self.cleaned_data
    #     name = data.get("name")
    #     qs = Project.objects.filter(name__icontains=name)
    #     if qs.exists():  # this is not right.
    #         self.add_error("name", f"{name} already exists in the database")
    #         # raise forms.ValidationError("This project already exists")
    #     return data

