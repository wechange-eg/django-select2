# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url
from django_select2 import views

urlpatterns = [
    url(r"^fields/auto.json$", views.auto_response_view, name="django_select2_central_json"),
]
