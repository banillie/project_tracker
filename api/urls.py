from django.urls import path

from django.urls import include, path

from . import views

from projects.views import ProjectListCreateAPIView, ProjectDetailAPIView
from engagements.views import EngagementDetailAPIView, EngagementListAPIView

urlpatterns = [
    path('', views.api_home),  # localhost8000/api

    path('projects/', ProjectListCreateAPIView.as_view()),
    path("projects/<int:pk>/", ProjectDetailAPIView.as_view()),
    # path('projects/list/', ProjectListAPIView.as_view()),

    path("engagements/<int:pk>/", EngagementDetailAPIView.as_view()),
    path("engagements/list/", EngagementListAPIView.as_view())
]