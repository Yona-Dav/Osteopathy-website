from django.urls import path
from . import views
from .views import CommonQuestionCreateView, CommonQuestionDeleteView, CommonQuestionUpdateView

urlpatterns = [
    path('commonQuestion/Add/', views.CommonQuestionCreateView.as_view(), name='common_quest_form'),
    path('<int:pk>/ deleteQuestion/', views.CommonQuestionDeleteView.as_view(), name='delete_question'),
    path('updateQuestion/<int:pk>/', views.CommonQuestionUpdateView.as_view(), name='update_question'),
    path('<int:pk>/ deleteReview/', views.ReviewDeleteView.as_view(), name='delete_review'),
    path('review/<int:review_id>/<int:published>', views.evaluate_review, name='eval_review'),

]