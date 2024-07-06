from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Log
from .serializers import LogSerializer

class LogViewSet(viewsets.ReadOnlyModelViewSet):
  """
  A viewset for viewing logs. Only read operations are allowed.
  Logs are ordered by timestamp in descending order.
  """
  queryset = Log.objects.all().order_by('-timestamp')
  serializer_class = LogSerializer
  permission_classes = [IsAuthenticated]
  