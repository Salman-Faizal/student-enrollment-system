from django.conf import settings
from django.core.exceptions import ValidationError
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Student
from .serializers import StudentSerializer
from funnel.models import FunnelStatus


class StudentViewSet(viewsets.ModelViewSet):
  queryset = Student.objects.all()
  serializer_class = StudentSerializer
  permission_classes = [IsAuthenticated]
  
  def perform_create(self, serializer):
    try:
      default_status = FunnelStatus.objects.get(name=settings.DEFAULT_FUNNEL_STATUS)
      serializer.save(current_status=default_status)
    except FunnelStatus.DoesNotExist:
      raise ValidationError(f"Default funnel status '{settings.DEFAULT_FUNNEL_STATUS}' does not exist.")
