from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from article.models import Article
from article.forms import ArticleForm
# Create your views here.

def articles(request):
    return render_to_response('article/articles.html',
                              {'articles' : Article.objects.all()})

def article(request, article_id):
    return render_to_response(request, 'article/article.html',
                              {'article' : Article.objects.get(id)})

def create_article(request):
    form = ArticleForm()
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/articles/all')

    return render(request, 'article/create_article.html',
                  {"form" : form})

