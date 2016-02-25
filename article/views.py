from django.shortcuts import render, render_to_response
from models import Article
from forms import ArticleForm
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template.context_processors import csrf

# Create your views here.

def articles(request):
    language = 'en-gb'
    session_language = 'en-gb'

    if 'lang' in request.COOKIES:
        language = request.COOKES['lang']

    if 'lang' in request.session:
       session_language = request.session['lang']

    return render_to_response('article/articles.html',
            {'articles' : Article.objects.all(),
             'language' : language,
             'session_language' : session_language})

def article(request, article_id=1):
    return render_to_response('article/article.html',
            {'article' : Article.objects.get(id=article_id) })

def language(request, language='en-gb'):
    response = HttpResponse("Setting language to %s" % language)

    response.set_cookie('lang', language)

    request.session['lang'] = language

    return response

def create_article(request):
    form = ArticleForm()
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/articles/all')
        else:
            form = ArticleForm()
            return render(request, 'article/create_article.html')
    else:
        return render(request, 'article/create_article.html',
                { "form" : form })

