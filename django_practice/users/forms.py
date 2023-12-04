from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


# inherits from UserCreationForm
class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    # required attributes for form
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']