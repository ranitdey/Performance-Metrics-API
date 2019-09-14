# -*- coding: utf-8 -*-
from __future__ import unicode_literals


# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from statistics_api.filters import UserFilter
from statistics_api.models import PerformanceMetric
from statistics_api.serializers import MetricSerializer
from rest_framework.permissions import AllowAny


class PerformanceListFilter(generics.ListAPIView):
    serializer_class = MetricSerializer
    queryset = PerformanceMetric.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filterset_class = UserFilter
    permission_classes = (AllowAny,)

    def get_queryset(self):
        queryset = self.queryset.extra(select={"cpi": "spend/installs"})
        fields = [field.name for field in PerformanceMetric._meta.get_fields()]
        fields.append('cpi')
        return queryset
