from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from cources.views import *

urlpatterns = [
    path('', CourseList.as_view(), name='course'),
    path('course_detail/<int:pk>', CourseDetail.as_view(), name='course_detail'),
    path('exercise/', ExerciseList.as_view(), name='exercise'),
    path('exercise_detail/<int:pk>', ExerciseDetail.as_view(),name='exercise_detail')
]


urlpatterns = format_suffix_patterns(urlpatterns)