from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import FunnelStatus
from .serializers import FunnelStatusSerializer


# Inheritting default crud operations from ModelViewSet for managing FunnelStatus instances
class FunnelStatusViewSet(viewsets.ModelViewSet):
    queryset = FunnelStatus.objects.all()
    serializer_class = FunnelStatusSerializer
    permission_classes = [IsAuthenticated]

    # explicitly defined this method for additional validation
    def create(self, request):
        serializer = FunnelStatusSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
