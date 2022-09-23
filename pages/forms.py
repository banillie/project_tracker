from django import forms

from ppdds.models import Comment
from django.utils.translation import ugettext_lazy as _


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            "ideas"
        ]

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['ideas'].label = "Ideas Section."

    def clean(self):
        user = self.cleaned_data.get('user')
        print(user)
        if user is None:
            raise forms.ValidationError(_("You must be logged in"))
        else:
            return user






