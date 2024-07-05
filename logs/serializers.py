from rest_framework import serializers
from .models import Log


class LogSerializer(serializers.ModelSerializer):
  class Meta:
    model = Log
    fields = ['id', 'student', 'previous_status', 'new_status', 'timestamp']
    read_only_fields = ['timestamp']
