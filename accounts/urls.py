from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from appointment.views import MyAppointmentsView

urlpatterns = [
    path('signup/', views.Signup.as_view(), name='signup'),
    path('login/', views.MyLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', views.activate, name='activate'),
    path('profile/', views.ProfileUpdateView.as_view(), name='my_profile'),
    path('medicalProfile/complete/', views.MedicalProfileCreateView.as_view(), name='add_medical'),
    path('medicalProfile/<int:pk>', views.MedicalProfileDetailView.as_view(), name='medical_profile'),
    path('mySchedules/', MyAppointmentsView.as_view(), name='my_schedules'),
]

