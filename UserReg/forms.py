from __future__ import unicode_literals

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from models import UserProfile

class RegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

        def save(self, commit=True):
            user = super(RegistrationForm, self).save(commit=False)
            user.email = self.cleaned_data['email']

            if commit:
                user.save()

            return user

class UserProfileForm(forms.ModelForm):
    email = forms.EmailField(label=u'Email')
    first_name = forms.CharField(label=u'First Name')
    last_name = forms.CharField(label=u'Last Name')

    def __init__(self, *args, **kw):
        super(UserProfileForm, self).__init__(*args, **kw)
        self.fields['email'].initial = self.instance.user.email
        self.fields['first_name'].initial = self.instance.user.first_name
        self.fields['last_name'].initial = self.instance.user.last_name

        self.fields.keyOrder = [
            'email',
            'first_name',
            'last_name',
            ]

    def save(self, *args, **kw):
        super(UserProfileForm, self).save(*args, **kw)
        user.email = self.cleaned_data.get('email')
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.save()

    class Meta:
        model = UserProfile
        fields = ('email', 'first_name', 'last_name')
