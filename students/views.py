from django.conf import settings
from django.core.exceptions import ValidationError
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from .models import Student
from .serializers import StudentSerializer
from funnel.models import FunnelStatus
from logs.models import Log
from logs.serializers import LogSerializer


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
  
  @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
  def update_status(self, request, pk=None):
    student = self.get_object()
    new_status_name = request.data.get('new_status')

    if not new_status_name:
      return Response({"error": "You must provide a new funnel-status for the student."}, status=status.HTTP_400_BAD_REQUEST)
    
    try:
      new_status = FunnelStatus.objects.get(name=new_status_name)
    except FunnelStatus.DoesNotExist:
      return Response({"error": f"The funnel-status '{new_status_name}' does not exist in the system."}, status=status.HTTP_400_BAD_REQUEST)
    
    previous_status = student.current_status

    if new_status == previous_status:
      return Response({"error": "The new funnel-status must be different from the existing funnel-status of the student."}, status=status.HTTP_400_BAD_REQUEST)
    
    student.current_status = new_status
    student.save()

    log = Log.objects.create(
      student=student,
      previous_status=previous_status,
      new_status=new_status
    )

    return Response({
      'student': StudentSerializer(student).data,
      'log': LogSerializer(log).data
    }, status=status.HTTP_200_OK)
