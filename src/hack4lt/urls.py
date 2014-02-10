from django.conf.urls import patterns, url, include
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from hack4lt.views import *


urlpatterns = patterns('',
    (r'^i18n/', include('django.conf.urls.i18n')),
)

urlpatterns += i18n_patterns('',
    url(r'^$', index_view, name='home'),
    url(r'^lectures/$', lectures_view, name='lectures'),
    url(r'^events/$', events_view, name='events'),
    url(r'^tasks/$', tasks_view, name='tasks'),
    url(r'^task/(?P<task_id>\d*)/$', task_view, name='task'),
    url(r'^about/$', about_view, name='about'),

    url(r'^login/$', login_view, name='login'),
    url(r'^logout/$', logout_view, name='logout'),
    url(r'^register/$', register_view, name='register'),
    url(r'^profile/$', profile_view, name='profile'),
)

urlpatterns += staticfiles_urlpatterns()
urlpatterns += patterns('',
    (r'^media/(?P<path>.*)$', 'django.views.static.serve',
     {'document_root': settings.MEDIA_ROOT}),
)
