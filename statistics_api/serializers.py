from rest_framework.serializers import ModelSerializer
from .models import PerformanceMetric
from rest_framework import serializers


class MetricSerializer(ModelSerializer):
    date = serializers.DateField(required=False)
    channel = serializers.CharField(required=False)
    country = serializers.CharField(required=False)
    os = serializers.CharField(required=False)
    impressions = serializers.IntegerField(required=False)
    clicks = serializers.IntegerField(required=False)
    installs = serializers.IntegerField(required=False)
    spend = serializers.DecimalField(max_digits=20, decimal_places=2, required=False)
    revenue = serializers.DecimalField(max_digits=20, decimal_places=2, required=False)
    cpi = serializers.FloatField(required=False)

    class Meta:
        model = PerformanceMetric
        fields = ['channel', 'country', 'impressions', 'clicks', 'date', 'spend', 'os', 'revenue', 'installs', 'cpi',]