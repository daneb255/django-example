from django import forms
from django.core import validators


class UserForm(forms.Form):
    first_name = forms.CharField(validators=[validators.MinLengthValidator(5)])
    last_name = forms.CharField()
    email = forms.EmailField()
    email2 = forms.EmailField(label="Enter E-Mail again!")

