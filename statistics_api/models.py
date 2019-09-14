# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class PerformanceMetric(models.Model):
    date = models.DateField(auto_now=False, auto_now_add=False)
    channel = models.CharField(max_length=100)
    country = models.CharField(max_length=10)
    os = models.CharField(max_length=20)
    impressions = models.IntegerField(default=0)
    clicks = models.IntegerField(default=0)
    installs = models.IntegerField(default=0)
    spend = models.DecimalField(max_digits=20, decimal_places=2)
    revenue = models.DecimalField(max_digits=20, decimal_places=2)
