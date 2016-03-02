from __future__ import unicode_literals
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class RegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('__all__')
