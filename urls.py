from django.conf.urls.defaults import *
import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	(r'^documents/', include('documents.folders_urls')),
	(r'^files/', include('documents.files_urls')),
    (r'^polls/', include('polls.urls')),
    (r'^admin/', include(admin.site.urls))
)
urlpatterns += patterns('',(r'^%s(?P<path>.*)$' % settings.MEDIA_URL[1:], 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}))