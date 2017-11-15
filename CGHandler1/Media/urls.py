from django.conf.urls import url, include

from Media.views import displayMedias, serverHandler, runMedia, MediaListApi, MediaApi, router

urlpatterns = [
    url(r'^media/medias/$', displayMedias, name="displayMedias"),
    url(r'^media/medias/(.+)', runMedia, name="runMedia"),
    url(r'^media/cgserver/(\w+)', serverHandler, name="serverHandlerFileName"),
    url(r'^api/media/$', MediaListApi),
    url(r'^api/media/(?P<id>[0-9]+)/$', MediaApi),
    url(r'^api/media/statistics/', include(router.urls)),
]