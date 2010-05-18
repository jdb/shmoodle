from django.conf.urls.defaults import *
from shmoodle.poll.views import poll,poll_handler,vote,vote_handler

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/doc/'      , include('django.contrib.admindocs.urls')),
    (r'^admin/'          , include(admin.site.urls)),
    (r'^$'               , poll),
    (r'poll_post'        , poll_handler),
    (r'^vote/\w{6}/?$'   , vote),
    (r'vote_post/\w{6}/?', vote_handler),
)
