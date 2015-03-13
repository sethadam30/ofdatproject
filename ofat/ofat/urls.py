from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'main.views.homepage', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^forums/', include('forums.urls', namespace='forums')),
    url(r'^admin/', include(admin.site.urls)),
)
