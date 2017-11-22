# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin

from sgo import settings



admin.autodiscover()

urlpatterns = [

    url(r'^', include(admin.site.urls), name='menu'),
    url(r'^explorer/', include('explorer.urls')),
    url(r'^admin/jsi18n/', 'django.views.i18n.javascript_catalog'),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# static files (images, css, javascript, etc.)
urlpatterns += patterns('',
    (r'^docs/(?P<path>.*)$',
    'django.views.static.serve',
    {'document_root': settings.MEDIA_ROOT}
    ))
urlpatterns += patterns('',
    (r'^static/(?P<path>.*)$',
    'django.views.static.serve',
    {'document_root':settings.STATIC_ROOT}
    ))
