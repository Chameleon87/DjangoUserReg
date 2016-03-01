from django.conf.urls import url, include
from views import article, articles, create_article 

urlpatterns = [
    url(r'^all/$', articles, name='all'),
    url(r'^get/(?P<id>\d+)/article.html', article, name='get'),
    url(r'^create/$', create_article, name='create'),
    #App urls 
    url(r'^accounts/', include('userprofiles.urls')),
]
