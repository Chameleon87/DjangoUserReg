from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Article(models.Model):
    article_id = models.AutoField(primary_key=True, default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    body = models.TextField()

    def __unicode__(self):
        return self.title
