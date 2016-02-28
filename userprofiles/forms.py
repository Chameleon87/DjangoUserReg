from django import forms
from userprofiles.models import UserProfile

class UserProfileForm(forms.ModelForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)

    class Meta:
        model = UserProfile
        fields = ('user' ,'first_name', 'last_name')

        def save(self, commit=True):
            userprofile = super(UserProfile, self).save(commit=True)
            user.email = self.cleaned_data['email']
            user.first_name = self.cleaned_data['first_name']
            user.last_name = self.cleaned_data['last_name']

            if commit:
                userprofile.save()

            return userprofile
