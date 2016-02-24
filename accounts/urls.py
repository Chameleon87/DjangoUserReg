from django.conf import settings
from django.conf.urls import patterns, include, url

urlpatterns = patterns('accounts.views',
        url(r'^login/$', 'login', name='login'),
        )
