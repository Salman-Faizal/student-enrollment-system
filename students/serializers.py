from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.ModelSerializer):
  # Displaying the current-status of the student as read-only
  current_status = serializers.ReadOnlyField(source='current_status.name')

  class Meta:
    model = Student
    fields = ['id', 'name', 'email', 'current_status', 'created_at', 'updated_at']
    read_only_fields = ['current_status', 'created_at', 'updated_at']
