from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.utils.translation import ugettext as _
from django.contrib.auth.decorators import login_required
from article.models import Article
from article.forms import ArticleForm

# Create your views here.
def articles(request):
    return render(request, 'article/articles.html',
                              {'articles' : Article.objects.all()})

@login_required
def article(request, article_id):
    return render(request, 'article/article.html',
                              {'article' : get_object_or_404(Article, id=article_id)})

@login_required
def edit_article(request, pk=None ):
    if pk:
        article = get_object_or_404(Article, pk=pk)
        if article.user != request.user:
            return HttpResponseForbidden()
    else:
        article = Article(user=request.user)

    if request.method == "POST":
        form = ArticleForm(request.POST, instance=article)
    else:
        form = ArticleForm(instance=article)

    if form.is_valid():
        form.save()
        redirect_url = reverse('all')
        return redirect(redirect_url)
    else:
        return render(request, 'article/create_article.html', {'form': form})
