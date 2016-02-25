from django.conf.urls import patterns, include, url
from . import views

urlpatterns = patterns('article.views',
        url(r'^$', views.articles, name='all'),
        url(r'^all/$', views.articles, name='all'),
        url(r'^get/(?P<article_id>\d+)/$', views.article, name='get'),
        url(r'^language/(?P<language>[a-z\-]+)/$', views.language),
        url(r'^create/$', views.create_article, name='create'),
)
