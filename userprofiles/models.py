from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from localflavor.us.models import PhoneNumberField, USZipCodeField, USSocialSecurityNumberField
from localflavor.us.us_states import STATE_CHOICES

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, related_name="profile", unique=True)
    email = models.EmailField()
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = PhoneNumberField(null=True)

    #Address
    address1 = models.CharField(max_length=100, null=True)
    address2 = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=50, null=True)
    state = models.CharField(max_length=50, null=True)
    zip_code = USZipCodeField(null=True)

    #Confidential
    ssn = USSocialSecurityNumberField(null=True)

    def __unicode__(self):
        return str(self.email)

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])
