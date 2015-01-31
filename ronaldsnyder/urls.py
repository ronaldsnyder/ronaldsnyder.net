from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ronaldsnyder.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', include('mysite.urls', namespace="mysite")),
    # url(r'^blog/', include('blog.urls')),
    url(r'^mysite/', include('mysite.urls', namespace="mysite")),
    url(r'^admin/', include(admin.site.urls)),
)
