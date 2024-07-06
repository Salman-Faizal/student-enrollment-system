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
        # checking if a FunnelStatus with the same name already exists
        name = request.data.get('name')
        if FunnelStatus.objects.filter(name=name).exists():
            return Response(
                {"Error": "A funnel-status with this name already exists in the system."},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = FunnelStatusSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
