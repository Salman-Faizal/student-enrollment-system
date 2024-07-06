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
    """
    Sets the default status for a new student during creation to DEFAULT_FUNNEL_STATUS (configured on the project settings).
    Raises a validation error if the default status does not exist in the database.
    """
    try:
      default_status = FunnelStatus.objects.get(name=settings.DEFAULT_FUNNEL_STATUS)
      serializer.save(current_status=default_status)
    except FunnelStatus.DoesNotExist:
      raise ValidationError(f"Default funnel status '{settings.DEFAULT_FUNNEL_STATUS}' does not exist.")
  
  @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
  def update_status(self, request, pk=None):
    """
    Custom action to update the current-status of a student.
    Validates the new status and creates a log entry for the status change.
    """
    student = self.get_object()
    new_status_name = request.data.get('new_status')

    # Checking if new status name is provided in the request
    if not new_status_name:
      return Response({"error": "You must provide a new funnel-status for the student."}, status=status.HTTP_400_BAD_REQUEST)
    
    # Validating the new-status by checking if it exists in the system
    try:
      new_status = FunnelStatus.objects.get(name=new_status_name)
    except FunnelStatus.DoesNotExist:
      return Response({"error": f"The funnel-status '{new_status_name}' does not exist in the system."}, status=status.HTTP_400_BAD_REQUEST)
    
    # Checking if the new-status is different from the existing current-status
    previous_status = student.current_status

    if new_status == previous_status:
      return Response({"error": "The new funnel-status must be different from the existing funnel-status of the student."}, status=status.HTTP_400_BAD_REQUEST)
    
    # Updating the student's current-status
    student.current_status = new_status
    student.save()

    # Creating a log entry for the status change
    log = Log.objects.create(
      student=student,
      previous_status=previous_status,
      new_status=new_status
    )

    # Returning the updated student and the created log-entry as a response
    return Response({
      'student': StudentSerializer(student).data,
      'log': LogSerializer(log).data
    }, status=status.HTTP_200_OK)
