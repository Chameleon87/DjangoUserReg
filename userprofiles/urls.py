from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^profile/$', views.user_profile, name="user_profile"),
    url(r'^edit_profile/$', views.edit_user_profile, name="edit_profile"),
]
