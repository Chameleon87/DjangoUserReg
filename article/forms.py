from django import forms
from article.models import Article
from django.contrib.auth.models import User

class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ('id', 'user', 'title', 'body')
