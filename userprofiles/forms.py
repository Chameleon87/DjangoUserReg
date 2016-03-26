from django.forms import ModelForm 
from userprofiles.models import UserProfile
from localflavor.us.forms import USStateSelect

class UserProfileForm(ModelForm):

    class Meta:
        model = UserProfile
        fields = ('__all__')
        exclude = ('user',)
