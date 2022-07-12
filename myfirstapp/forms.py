from django import forms
from django.core import validators
from myfirstapp.models import User


class UserForm(forms.ModelForm):
    first_name = forms.CharField(validators=[validators.MinLengthValidator(5)])
    email2 = forms.EmailField(label="Enter E-Mail again!")

    def clean(self):
        email = self.cleaned_data['email']
        email2 = self.cleaned_data['email2']

        if email != email2:
            raise forms.ValidationError("EMail not match!")

        return self.cleaned_data

    class Meta:
        model = User
        fields = '__all__'

