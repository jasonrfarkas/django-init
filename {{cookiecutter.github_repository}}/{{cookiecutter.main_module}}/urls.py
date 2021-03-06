# -*- coding: utf-8 -*-
"""Root url routering file.

You should put the url config in their respective app putting only a
refernce to them here.
"""
from __future__ import absolute_import, unicode_literals

# Third Party Stuff
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views import defaults as dj_default_views
from django.views.generic import TemplateView

# {{ cookiecutter.project_name }} Stuff
from {{ cookiecutter.main_module }}.base import views as base_views

from .routers import router

handler500 = base_views.server_error

# Top Level Pages
# ==============================================================================
urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='pages/home.html'), name="home"),
    url(r'^about/$', TemplateView.as_view(template_name='pages/about.html'), name="about"),
    # Your stuff: custom urls go here
]

urlpatterns += [

    url(r'^(?P<filename>(robots.txt)|(humans.txt))$',
        base_views.root_txt_files, name='root-txt-files'),

    # Rest API
    url(r'^api/', include(router.urls)),

    # Browsable API
    url(r'^api/auth-n/', include('rest_framework.urls', namespace='rest_framework')),

    # Django Admin
    url(r'^admin/', include(admin.site.urls)),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    # Livereloading
    urlpatterns += [url(r'^devrecargar/', include('devrecargar.urls', namespace='devrecargar'))]

    urlpatterns += [
        url(r'^400/$', dj_default_views.bad_request, kwargs={'exception': Exception("Bad Request!")}),
        url(r'^403/$', dj_default_views.permission_denied, kwargs={'exception': Exception("Permission Denied!")}),
        url(r'^404/$', dj_default_views.page_not_found, kwargs={'exception': Exception("Not Found!")}),
        url(r'^500/$', handler500),
    ]
