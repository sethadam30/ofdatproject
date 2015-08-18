from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.views import login, logout
from django.views.generic import TemplateView

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'main.views.homepage', name='home'),
    url(r'^forum$', TemplateView.as_view(template_name='main/forum.html'), name='forum'),
    # url(r'^blog/', include('blog.urls')),

    #(r'^forum/', include('pybb.urls', namespace='pybb')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$', login),
    url(r'^accounts/logout/$', logout),
)
