from django.db import models
from students.models import Student
from funnel.models import FunnelStatus


class Log(models.Model):
  """
  Foreign key association and behavior:
  If any of the associated student, previous_status, or new_status is deleted from the database,
  then the log object will also be deleted.
  """
  student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='logs')
  previous_status = models.ForeignKey(FunnelStatus, on_delete=models.CASCADE, related_name='previous_logs')
  new_status = models.ForeignKey(FunnelStatus, on_delete=models.CASCADE, related_name='new_logs')
  timestamp = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return f"Log for '{self.student.name}' from '{self.previous_status.name}' to '{self.new_status.name}' at {self.timestamp}"
