from django.db.models import Count
from attendance.models import Attendance

def monthly_report(month):
    return Attendance.objects.filter(
        date__month=month
    ).values('user').annotate(total_days=Count('id'))
