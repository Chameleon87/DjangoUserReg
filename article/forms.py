from django import forms
from article.models import Article
from django.contrib.auth.models import User

class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ('id', 'user', 'title', 'body', 'likes')

        def save(self, commit=True):
            user = super(ArticleForm, self).save(commit=False)
            Article.id = self.cleaned_data['id']
            Article.title = self.cleaned_data['title']
            Article.body = self.cleaned_data['body']

            if commit:
                Article.save()

            return Article
