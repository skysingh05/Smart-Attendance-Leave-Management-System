from django.conf import settings
from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Attendance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    check_in = models.DateTimeField()
    check_out = models.DateTimeField(null=True, blank=True)
    date = models.DateField(auto_now_add=True)

    def working_hours(self):
        if self.check_out:
            return self.check_out - self.check_in
        return None

    def __str__(self):
        return f"{self.user} - {self.date}"
    
class Leave(models.Model):
    LEAVE_STATUS = (
        ('PENDING', 'Pending'),
        ('APPROVED', 'Approved'),
        ('REJECTED', 'Rejected'),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField()
    status = models.CharField(max_length=10, choices=LEAVE_STATUS, default='PENDING')
    applied_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} ({self.start_date} - {self.end_date})"