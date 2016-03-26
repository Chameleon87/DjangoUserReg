from django.forms import ModelForm 
from userprofiles.models import UserProfile

class UserProfileForm(ModelForm):

    class Meta:
        model = UserProfile
        fields = ('__all__')
        exclude = ('user',)
