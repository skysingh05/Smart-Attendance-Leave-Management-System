from rest_framework import serializers
from attendance.models import Attendance, Leave

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = '__all__'

class LeaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leave
        fields = '__all__'
        read_only_fields = ['user', 'status']


from attendance.models import Leave

class LeaveListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leave
        fields = [
            'id',
            'user',
            'start_date',
            'end_date',
            'reason',
            'status',
            'applied_at'
        ]
