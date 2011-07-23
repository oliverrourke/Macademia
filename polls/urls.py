from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', 'polls.views.index'),
    (r'^(?P<poll_id>\d+)/$', 'polls.views.detail'),
    (r'^(?P<poll_id>\d+)/results/$', 'polls.views.results'),
    (r'^(?P<poll_id>\d+)/vote/$', 'polls.views.vote'),
)
