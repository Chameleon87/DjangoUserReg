from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.template import RequestContext
from django.utils.translation import ugettext as _
from django.contrib.auth.decorators import login_required
from article.models import Article
from article.forms import ArticleForm

# Create your views here.
def articles(request):
    return render_to_response('article/articles.html',
                              {'articles' : Article.objects.all()})

def article(request, article_id):
    return render_to_response('article/article.html',
                              {'article' : get_object_or_404(Article, id=article_id)})

@login_required
def edit_article(request, pk=None, template_name='article/create_article.html'):
    if pk:
        article = get_object_or_404(Article, pk=pk)
        if article.user != request.user:
            return HttpResponseForbidden()
    else:
        article = Article(user=request.user)

    if request.method == "POST":
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, _('Article correctly saved.'))
            # If the save was successful, redirect to another page
            redirect_url = reverse('all')
            return HttpResponseRedirect(redirect_url)

    else:
        form = ArticleForm(instance=article)

    return render_to_response(template_name, {
        'form': form,
    }, context_instance=RequestContext(request))
