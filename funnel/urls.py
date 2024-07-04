from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FunnelStatusViewSet

# Registering ViewSet using a router
# to automate the creation of API URLs 
router = DefaultRouter()
router.register(r'statuses', FunnelStatusViewSet, basename='status')

urlpatterns = [
  path('', include(router.urls)),
]
