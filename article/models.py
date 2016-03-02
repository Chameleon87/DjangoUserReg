from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Article(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    body = models.TextField()

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/articles/get/%i" % self.pk
