from django.contrib import admin
from .models import FunnelStatus

# Registered FunnelStatus model for accessing in Django admin interface
# incase, for future administrative tasks 
admin.site.register(FunnelStatus)
