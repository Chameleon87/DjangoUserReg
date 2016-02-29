from django.conf.urls import url, include
from article.views import articles, article, create_article

urlpatterns = [
    url(r'^$', articles, name='all'),
    url(r'^all/$', articles, name='all'),
    url(r'^get/(?P<article_id>\d+)/$', article, name='get'),
    url(r'^create/$', create_article, name='create'),
    #App urls
    url(r'^accounts/', include('userprofiles.urls')),
]
