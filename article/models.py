from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Article(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    body = models.TextField()
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    likes = models.IntegerField(default=0)

    def __unicode__(self):
        return self.title
