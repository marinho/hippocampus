from django.conf.urls.defaults import *

from test_app.models import Widget

id_dict = {
    'queryset': Widget.objects.all(),
    'hippocampus': Widget,
}

slug_dict = {
    'queryset': Widget.objects.all(),
    'hippocampus': Widget,
    'slug_field': 'slug'
}

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    (r'^widgets/(?P<object_id>\d+)/$', 'django.views.generic.list_detail.object_detail', id_dict),
    (r'^widgets/(?P<slug>[\w-]+)/$', 'django.views.generic.list_detail.object_detail', slug_dict),
    (r'^hippocampus/', include('hippocampus.urls')),
)
