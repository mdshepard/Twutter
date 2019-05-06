from django import forms
from django.utils.html import strip_tags  # noqa someone told me these were necessary and I don't really understand...

from .models import Twuut


class TwuutForm(forms.ModelForm):
    body = forms.CharField(
        required=True,
        widget=forms.widgets.Textarea(attrs={'placeholder': 'Twuut', 'class': 'form-control'}
            )
        )


    class Meta:
        model = Twuut
        exclude = ('user', )
