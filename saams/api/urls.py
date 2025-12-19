from django.urls import path
from . import views

urlpatterns = [
    path('check-in/', views.CheckInView.as_view(), name='check-in'),
    path('check-out/', views.CheckOutView.as_view(), name='check-out'),

    path('leave/apply/', views.ApplyLeaveView.as_view(), name='apply-leave'),
    path('leave/update/<int:leave_id>/', views.UpdateLeaveStatusView.as_view(), name='update-leave'),
    
    path('leave/my/', views.MyLeaveListView.as_view(), name='my-leave-list'),
    path('leave/all/', views.AllLeaveListView.as_view(), name='all-leave-list'),

    path('attendance/my/monthly/', views.MyMonthlyAttendanceView.as_view(), name='my-monthly-attendance'),
    path('attendance/admin/daily/', views.DailyAttendanceReportView.as_view(), name='daily-attendance'),
    
    path('attendance/my/hours/', views.MyWorkingHoursView.as_view(), name='my-working-hours'),

]
