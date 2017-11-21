from django.conf.urls import url, include

from rundown.views import loadMedias, testCustomTags

urlpatterns = [
    url(r'^rundown/$', loadMedias, name="loadMedias"),
    url(r'^rundown/test/customtags/$', testCustomTags, name="testCustomTags"),
]