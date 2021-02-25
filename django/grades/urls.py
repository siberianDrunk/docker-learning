
from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns

from grades import views

urlpatterns = [

    path('grades/', views.GradesList.as_view()),
    path('directions/', views.DirectionList.as_view()),

    path('grades/<int:pk>/', views.GradesDetail.as_view()),

]
