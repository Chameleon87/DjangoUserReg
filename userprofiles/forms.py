from django.forms import ModelForm 
from userprofiles.models import UserProfile

class UserProfileForm(ModelForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)

    class Meta:
        model = UserProfile
        fields = ('__all__')
        exclude = ('user',)
