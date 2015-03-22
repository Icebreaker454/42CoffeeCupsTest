from django.conf.urls import patterns, include, url
from django.contrib import admin

from ticket1.views import IndexView

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', IndexView.as_view(), name='home')
)
