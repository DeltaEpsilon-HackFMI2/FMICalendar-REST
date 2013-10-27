from django.conf.urls import patterns, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^schedule/$', 'schedule.views.menu_map'),
    url(r'^sendfile/$', 'schedule.views.send_file'),
)
