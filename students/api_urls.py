from django.urls import path
from . import api_views

urlpatterns = [
    path('grades/', api_views.GradeListCreateAPIView.as_view(), name='grade-list'),
    path('subjects/', api_views.SubjectListCreateAPIView.as_view(), name='subject-list'),
]
