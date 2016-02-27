from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User)

    def __unicode__(self):
        return str(self)

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])
