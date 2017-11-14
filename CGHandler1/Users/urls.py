from django.conf.urls import url

from Media.views import displayMedias, serverHandler
from Users.views import createuser, MyView, displayUsers

urlpatterns = [
    url(r'^user/create/', createuser, name="createuser"),
    url(r'^users/test/$', MyView.as_view()),
    url(r'^user/users/', displayUsers, name="displayUsers"),
]