from django.urls import path
from . import views

urlpatterns = [
    path('', views.About.as_view(), name='about'),
    path('contact/', views.ContactCreateView.as_view(), name='contact'),
    path('osteopathy/', views.Osteopathy.as_view(), name='osteopathy'),
    path('commonQuestion/', views.CommonQuestionView.as_view(), name='common_questions'),
    path('askQuestion/', views.AskQuestionCreateView.as_view(), name='ask_question'),
    path('review/add/', views.ReviewCreateView.as_view(), name='add_review'),
    path('review/', views.ReviewView.as_view(), name='reviews'),
]

