"""UserReg URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
#Django imports
from django.conf.urls import url, include
from django.contrib import admin
#App urls
from article import urls
from userprofiles import urls
#Local urls
from UserReg.views import index, login, auth_view, logout, invalid_login, register_user

urlpatterns = [
    #App urls
    url(r'^articles/', include('article.urls')),
    url(r'^accounts/', include('userprofiles.urls')),
    #Home urls
    url(r'^$', index, name='home'),
    url(r'^index/$', index, name='home'),
    #User auth urls
    url(r'^accounts/login/$', login, name='login'),
    url(r'^accounts/auth/$', auth_view),
    url(r'^accounts/logout/$', logout, name='logout'),
    url(r'^accounts/invalid/$', invalid_login),
    url(r'^accounts/user_exists/$', register_user),
    url(r'^accounts/register/$', register_user, name='register'),
    #Admin url
    url(r'^admin/', admin.site.urls),
]
