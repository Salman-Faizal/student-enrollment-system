from rest_framework import serializers
from .models import FunnelStatus


class FunnelStatusSerializer(serializers.ModelSerializer):
  class Meta:
    model = FunnelStatus
    fields = ['id', 'name', 'created_at', 'updated_at']
    read_only_fields = ['created_at', 'updated_at']
