from django.conf.urls import url
from . import views


urlpatterns = [
    url(regex=r'^$', view=views.UserListView.as_view(), name='list'),
    url(regex=r'^create/$', view=views.UserCreateView.as_view(), name='create'),
    url(regex=r'^edit/(?P<username>[\w.@+-]+)/$', view=views.UserEdit.as_view(), name='edit'),
    url(regex=r'^delete/(?P<username>[\w.@+-]+)/$', view=views.UserDelete.as_view(), name='delete'),
    url(regex=r'^(?P<username>[\w.@+-]+)/$', view=views.UserDetailView.as_view(), name='detail'),
]