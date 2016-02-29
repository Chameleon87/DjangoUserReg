from __future__ import unicode_literals
from django.contrib.auth.forms import UserCreationForm
from userprofiles.models import User


class RegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
