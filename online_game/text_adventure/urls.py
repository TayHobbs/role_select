from django.conf.urls import patterns, url
from text_adventure import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index')
)
