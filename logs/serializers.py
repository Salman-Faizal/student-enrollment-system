from rest_framework import serializers
from .models import Log
from students.models import Student
from funnel.models import FunnelStatus


class LogSerializer(serializers.ModelSerializer):
  # Customizing the representation of fields: student(as his/her email), previous_status(as name), and new_status(as name).
  student = serializers.EmailField(source='student.email', read_only=True)
  previous_status = serializers.CharField(source='previous_status.name', read_only=True)
  new_status = serializers.CharField(source='new_status.name', read_only=True)

  class Meta:
    model = Log
    fields = ['id', 'student', 'previous_status', 'new_status', 'timestamp']
    read_only_fields = ['timestamp']  # Ensuring that, 'timestamp' is read-only and auto-generated
