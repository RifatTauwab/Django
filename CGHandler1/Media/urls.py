from django.conf.urls import url

from Media.views import displayMedias, serverHandler, runMedia

urlpatterns = [
    url(r'^media/medias/$', displayMedias, name="displayMedias"),
    url(r'^media/medias/(.+)', runMedia, name="runMedia"),
    url(r'^media/cgserver/(\w+)', serverHandler, name="serverHandlerFileName"),
]