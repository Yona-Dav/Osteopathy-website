from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import CommonQuestionCreateView, CommonQuestionDeleteView, CommonQuestionUpdateView

urlpatterns = [
    path('commonQuestion/Add/', views.CommonQuestionCreateView.as_view(), name='common_quest_form'),
    path('<int:pk>/ deleteQuestion/', views.CommonQuestionDeleteView.as_view(), name='delete_question'),
    path('updateQuestion/<int:pk>/', views.CommonQuestionUpdateView.as_view(), name='update_question'),
    path('<int:pk>/ deleteReview/', views.ReviewDeleteView.as_view(), name='delete_review'),
    path('review/<int:review_id>/<int:published>', views.evaluate_review, name='eval_review'),
    path('exercise/Add/', views.ExerciseCreateView.as_view(), name='add_exercise'),
    path('<int:pk>/ deleteExercise/', views.ExerciseDeleteView.as_view(), name='delete_exercise'),
    path('updateExercise/<int:pk>/', views.ExerciseUpdateView.as_view(), name='update_exercise'),
    path('exercise/', views.ExerciseListView.as_view(), name='exercises'),
    path('exercises/category/<int:category_id>/', views.category_exercises, name='category_exercises'),
    path('exercises/category/', views.CategoryListView.as_view(), name='categories'),
    path('exercises/detail/<int:pk>/',views.ExerciseDetailView.as_view(), name='detail_ex')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)