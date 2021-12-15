from django.urls import path, include
from . import views

urlpatterns = [
    path('schedule/add/', views.ScheduleCreateView.as_view(), name='add_schedule'),
    path('schedule/', views.ScheduleView.as_view(), name='schedules'),
    path('<int:pk>/deleteSchedule/', views.ScheduleDeleteView.as_view(), name='delete_schedule'),
    path('updateSchedule/<int:pk>/', views.ScheduleUpdateView.as_view(), name='update_schedule'),
    path('bookedSchedule/', views.ScheduleBookedView.as_view(), name='booked_schedule'),
    path('schedule/<int:schedule_id>/<int:booked>/', views.book_appointment, name='book_appointment'),
    path('mySchedules/<int:schedule_id>/<int:canceled>/', views.cancel_appointment, name='cancel_appointment'),
    path('schedule/date/<slug:date_id>/', views.see_date_appointment, name='date_appointment')

]