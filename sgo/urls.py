# -*- coding: utf-8 -*-

#from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.http import HttpResponse

from sgo import settings

from django.views.generic import list
from django.views.generic import RedirectView
from django.core.urlresolvers import reverse_lazy
from . import views


admin.autodiscover()

urlpatterns = [

    url(r'^', include(admin.site.urls), name='menu'),
    url(r'^backup/$',views.run_backup, name='backup'),

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
