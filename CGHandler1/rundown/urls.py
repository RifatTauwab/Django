from django.conf.urls import url, include

from rundown.views import loadMedias

urlpatterns = [
    url(r'^rundown/$', loadMedias, name="loadMedias"),
]