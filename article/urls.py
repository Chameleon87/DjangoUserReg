from django.conf.urls import url, include
from article.views import articles, article, edit_article

urlpatterns = [
    url(r'^all/$', articles, name='all'),
    url(r'^get/(?P<article_id>\d+)/$', article, name='get'),
    url(r'^edit/$', edit_article, name='edit'),
    #App urls
    url(r'^accounts/', include('userprofiles.urls')),
]
