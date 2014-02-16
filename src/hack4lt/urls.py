from django.conf.urls import patterns, url, include
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from hack4lt.views import account, basic, task


urlpatterns = patterns('',
    (r'^i18n/', include('django.conf.urls.i18n')),
)

urlpatterns += i18n_patterns('',
    url(r'^$', basic.index_view, name='home'),
    url(r'^lectures/$', basic.lectures_view, name='lectures'),
    url(r'^events/$', basic.events_view, name='events'),
    url(r'^task/(?P<task_id>\d*)/$', basic.task_view, name='task'),
    url(r'^about/$', basic.about_view, name='about'),

    url(r'^tasks/$', task.TaskInfoList.as_view(), name='tasks'),
    url(r'^task/(?P<slug>[a-z0-9-_]+)/do/$', task.do_task_view, name='do-task'),
    url(r'^task/(?P<slug>[a-z0-9-_]+)/create/$', task.TaskResultCreate.as_view(), name='create-task'),
    url(r'^task/(?P<slug>[a-z0-9-_]+)/update/$', task.TaskResultUpdate.as_view(), name='update-task'),
    url(r'^task/(?P<slug>[a-z0-9-_]+)/view/$', task.TaskResultDetail.as_view(), name='view-task'),

    url(r'^task/(?P<slug>[a-z0-9-_]+)/comment/$', task.user_comment_view, name='comment-task'),
    url(r'^task/(?P<pk>\d*)/admin/comment/$', task.admin_comment_view, name='admin-comment-task'),
    url(r'^task/(?P<pk>\d*)/check/$', task.TaskResultCheckUpdate.as_view(), name='check-task'),

    url(r'^task/info/new/$', task.TaskInfoCreate.as_view(), name='new-task-info'),
    url(r'^task/(?P<pk>\d*)/info/update/$', task.TaskInfoUpdate.as_view(), name='update-task-info'),
    url(r'^task/(?P<pk>\d*)/info/delete/$', task.TaskInfoDelete.as_view(), name='delete-task-info'),


    url(r'^login/$', account.login_view, name='login'),
    url(r'^logout/$', account.logout_view, name='logout'),
    url(r'^register/$', account.register_view, name='register'),
    url(r'^profile/$', account.ProfileDetailView.as_view(), name='profile'),
    url(r'^profile/edit/$', account.profile_view, name='profile-edit'),
    url(r'^admin/$', basic.admin_view, name='admin-dashboard'),
)

urlpatterns += staticfiles_urlpatterns()
urlpatterns += patterns('',
    (r'^media/(?P<path>.*)$', 'django.views.static.serve',
     {'document_root': settings.MEDIA_ROOT}),
)
