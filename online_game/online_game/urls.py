from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^$', include('text_adventure.urls')),
    url(r'^text_adventure/', include('text_adventure.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
