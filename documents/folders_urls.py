from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^(.*)$', 'documents.views.main'),
)
#f = Folder(name = folder_name, parent_folder = 1, folder_path = 'Home/Papers')