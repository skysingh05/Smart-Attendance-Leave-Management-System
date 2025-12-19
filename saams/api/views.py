from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.utils import timezone
from attendance.models import Attendance, Leave
from datetime import date
from rest_framework import status
from api.serializers import LeaveListSerializer


class CheckInView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        Attendance.objects.create(
            user=request.user,
            check_in=timezone.now()
        )
        return Response({"message": "Checked in successfully"})
    

class CheckOutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        today = date.today()

        attendance = Attendance.objects.filter(
            user=request.user,
            date=today,
            check_out__isnull=True
        ).first()

        if not attendance:
            return Response(
                {"error": "No active check-in found for today"},
                status=400
            )

        attendance.check_out = timezone.now()
        attendance.save()

        return Response({"message": "Checked out successfully"})



class ApplyLeaveView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        start_date = request.data.get('start_date')
        end_date = request.data.get('end_date')
        reason = request.data.get('reason')

        # Overlapping leave check
        overlapping = Leave.objects.filter(
            user=request.user,
            start_date__lte=end_date,
            end_date__gte=start_date,
            status__in=['PENDING', 'APPROVED']
        )

        if overlapping.exists():
            return Response(
                {"error": "Leave already exists for selected dates"},
                status=status.HTTP_400_BAD_REQUEST
            )

        Leave.objects.create(
            user=request.user,
            start_date=start_date,
            end_date=end_date,
            reason=reason
        )

        return Response(
            {"message": "Leave applied successfully"},
            status=status.HTTP_201_CREATED
        )

class UpdateLeaveStatusView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, leave_id):
        if not request.user.is_staff:
            return Response(
                {"error": "Permission denied"},
                status=status.HTTP_403_FORBIDDEN
            )

        status_value = request.data.get('status')

        if status_value not in ['APPROVED', 'REJECTED']:
            return Response(
                {"error": "Invalid status"},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            leave = Leave.objects.get(id=leave_id)
        except Leave.DoesNotExist:
            return Response(
                {"error": "Leave not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        leave.status = status_value
        leave.save()

        return Response(
            {"message": f"Leave {status_value.lower()} successfully"}
        )


class MyLeaveListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        leaves = Leave.objects.filter(user=request.user).order_by('-applied_at')
        serializer = LeaveListSerializer(leaves, many=True)
        return Response(serializer.data)


class AllLeaveListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        if not request.user.is_staff:
            return Response(
                {"error": "Permission denied"},
                status=status.HTTP_403_FORBIDDEN
            )

        leaves = Leave.objects.all().order_by('-applied_at')
        serializer = LeaveListSerializer(leaves, many=True)
        return Response(serializer.data)


from django.db.models import Count

class MyMonthlyAttendanceView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        month = request.query_params.get('month')  # format: YYYY-MM

        if not month:
            return Response(
                {"error": "month parameter is required (YYYY-MM)"},
                status=status.HTTP_400_BAD_REQUEST
            )

        year, month = map(int, month.split('-'))

        records = Attendance.objects.filter(
            user=request.user,
            date__year=year,
            date__month=month
        )

        total_days = records.values('date').distinct().count()
        total_checkins = records.count()

        return Response({
            "total_working_days": total_days,
            "total_checkins": total_checkins
        })


class DailyAttendanceReportView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        if not request.user.is_staff:
            return Response(
                {"error": "Permission denied"},
                status=status.HTTP_403_FORBIDDEN
            )

        date_param = request.query_params.get('date')  # YYYY-MM-DD

        if not date_param:
            return Response(
                {"error": "date parameter is required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        records = Attendance.objects.filter(date=date_param)

        data = []
        for r in records:
            data.append({
                "user": r.user.username,
                "check_in": r.check_in,
                "check_out": r.check_out
            })

        return Response(data)


from django.db.models import F, ExpressionWrapper, DurationField
from django.db.models.functions import Coalesce

class MyWorkingHoursView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        records = Attendance.objects.filter(
            user=request.user,
            check_out__isnull=False
        ).annotate(
            duration=ExpressionWrapper(
                F('check_out') - F('check_in'),
                output_field=DurationField()
            )
        )

        total_seconds = sum([r.duration.total_seconds() for r in records])

        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60

        return Response({
            "total_hours": int(hours),
            "total_minutes": int(minutes)
        })
