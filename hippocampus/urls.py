from django.conf.urls.defaults import *

urlpatterns = patterns('hippocampus.views',
    url(r'^exit/$', 'log_exit', name='hippocampus_log_exit'),
)
