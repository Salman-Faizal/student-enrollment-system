from django.db import models
from funnel.models import FunnelStatus


class Student(models.Model):
  name = models.CharField(max_length=100)
  email = models.EmailField(unique=True)    # Email address of students set to unique (based on the database design)
  current_status = models.ForeignKey(FunnelStatus, on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return f'{self.name} ({self.email} - Status: {self.current_status.name})'
