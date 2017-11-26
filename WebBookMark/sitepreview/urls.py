from django.conf.urls import url, include

from sitepreview.views import home, router

urlpatterns = [
    url(r'^bookmark/$', home, name="home"),
    url(r'^api/', include(router.urls)),
]