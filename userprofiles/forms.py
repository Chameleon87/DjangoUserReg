from django import forms
from userprofiles.models import UserProfile

class UserProfileForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)

    class Meta:
        model = UserProfile
        fields = ('email', 'first_name', 'last_name',)
