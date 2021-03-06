from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic.base import RedirectView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^users/', include('user.urls', namespace='user')),
    url(r'^.*$', RedirectView.as_view(pattern_name='user:list', permanent=False))
]
