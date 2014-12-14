from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

import views

urlpatterns = patterns('',

    url(r'^$', views.index, name='index'),
    url(r'^$', views.signup, name='signup'),
    url(r'^$', views.login, name='login'),

    #url(r'^signup/$', views.signup, name='signup'),

    #url(r'^login/$', views.login, name='s'),
)
