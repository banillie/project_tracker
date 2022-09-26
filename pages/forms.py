from django import forms
from ppdds.models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            "ideas"
        ]

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['ideas'].label = "Ideas Section."

    def clean(self, *args, **kwargs):
        user = self.request
        if user.is_anonymous:
            raise forms.ValidationError("You must be logged in")









