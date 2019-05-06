from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.utils.html import strip_tags  # noqa (I did this just to stop getting the error, not sure if it's pep8's false flag, or actually not being used?)


class SignupForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.widgets.TextInput( attrs={'placeholder': 'Email', 'class': 'form-control'})) # noqa
    first_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder': 'First Name', 'class': 'form-control'})) # noqa
    last_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder': 'Last Name', 'class': 'form-control'})) # noqa
    username = forms.CharField(widget=forms.widgets.TextInput(attrs={'placeholder': 'Username', 'class': 'form-control'})) # noqa
    password1 = forms.CharField(widget=forms.widgets.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control'})) # noqa
    password2 = forms.CharField(widget=forms.widgets.PasswordInput(attrs={'placeholder': 'Password Confirmation', 'class': 'form-control'})) # noqa


class Meta:
    fields = ['email', 'username', 'first_name', 'last_name', 'password1', 'password2'] # noqa
    model = User


class SigninForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.widgets.TextInput(
            attrs={'placeholder': 'Username',
                   'class': 'form-control'
                   }
            )
        )
    password = forms.CharField(
        widget=forms.widgets.PasswordInput(
            attrs={'placeholder': 'Password',
                   'class': 'form-control'}
            )
        )
