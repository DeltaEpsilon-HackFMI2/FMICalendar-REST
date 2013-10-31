from django.conf.urls import patterns, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^schedule/$', 'schedule.views.menu_map'),
    url(r'^student/(?P<fn>\d+)/$', 'schedule.views.by_student_fn'),
    url(r'^group/(?P<group_id>\d+)/$', 'schedule.views.by_group_id'),
    url(r'^sendfile/$', 'schedule.views.send_file'),
)
