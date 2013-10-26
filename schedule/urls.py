from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^schedule/$', 'schedule.views.menu_map'),
)
