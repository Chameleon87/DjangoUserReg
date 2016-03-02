from django.conf.urls import url
from userprofiles.views import user_profile, edit_user_profile


urlpatterns = [
    url(r'^profile/$', user_profile, name="user_profile"),
    url(r'^edit_profile/$', edit_user_profile, name="edit_profile"),
]
