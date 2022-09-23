from django import forms

from ppdds.models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            "ideas"
        ]

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['ideas'].label = "Ideas Section."



