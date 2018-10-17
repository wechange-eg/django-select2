# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import include, url
from django.views.generic import TemplateView
from django.contrib import admin

admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', TemplateView.as_view(template_name="index.html"), name='home'),
    url(r'^test/', include('testapp.testmain.urls')),
    url(r'^ext/', include('django_select2.urls')),
]
