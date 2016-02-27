from django.conf.urls import include, url
from . import views
from UserReg.urls import urls

urlpatterns = [
        url(r'^profile/$', views.user_profile),
]
