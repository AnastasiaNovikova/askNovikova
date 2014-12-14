# coding=utf-8
from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static

from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

admin.autodiscover()

urlpatterns = patterns('',

    #url(r'^admin_tools/', include('admin_tools.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^', include('askMe.urls')),
)

if settings.DEBUG:

    import debug_toolbar
    urlpatterns += patterns('',
        url(r'^__debug__/', include(debug_toolbar.urls))
    )

    if settings.MEDIA_ROOT:

        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    if settings.STATIC_ROOT:

        urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)



urlpatterns += staticfiles_urlpatterns()
