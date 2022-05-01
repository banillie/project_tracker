from django.urls import path

from django.urls import include, path

from . import views

from projects.urls import ProjectCreateAPIView, ProjectDetailAPIView, ProjectListAPIView
from engagements.urls import EngagementDetailAPIView

urlpatterns = [
    path('', views.api_home),  # localhost8000/api

    path('projects/', ProjectCreateAPIView.as_view()),
    path("projects/<int:pk>/", ProjectDetailAPIView.as_view()),
    path('projects/list/', ProjectListAPIView.as_view()),

    path("engagements/<int:pk>/", EngagementDetailAPIView.as_view()),
]