# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from statistics_api.models import PerformanceMetric

admin.site.register(PerformanceMetric)
