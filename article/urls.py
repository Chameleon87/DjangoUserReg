from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.articles, name='all'),
    url(r'^all/$', views.articles, name='all'),
    url(r'^get/(?P<id>\d+)/$', views.article, name='get'),
    url(r'^language/(?P<language>[a-z\-]+)/$', views.language),
    url(r'^create/$', views.create_article, name='create'),
    #App urls 
    url(r'^accounts/', include('userprofiles.urls')),
]
