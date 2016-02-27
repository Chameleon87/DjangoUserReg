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
from django.conf.urls import url, include
from django.contrib import admin
from . import views
#App urls
from article import urls
from userprofiles import urls

urlpatterns = [
		#App urls
        url(r'^articles/', include('article.urls')),
		url(r'^accounts/', include('userprofiles.urls')),

        url(r'^$', views.index, name='home'),
        url(r'^index/$', views.index, name='home'),
        #User auth urls
        url(r'^accounts/login/$', views.login, name='login'),
        url(r'^accounts/auth/$', views.auth_view),
        url(r'^accounts/logout/$', views.logout, name='logout'),
        url(r'^accounts/loggedin/$', views.loggedin, name='loggedin'),
        url(r'^accounts/invalid/$', views.invalid_login),
        url(r'^accounts/user_exists/$', views.register_user),
        url(r'^accounts/register/$', views.register_user, name='register'),
        url(r'^accounts/register_success/$', views.register_success, name='register_success'),
        #Admin url
        url(r'^admin/', admin.site.urls),
]
