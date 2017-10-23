from django.conf.urls import url
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    url(regex=r'^list/$', view=views.UserListView.as_view(), name='user_list'),
]