from django.urls import path

# from . import views

from projects.views import ProjectListAPIView
from engagements.views import EngagementListAPIView

urlpatterns = [
    # path('', views.api_home),
    path("projects/", ProjectListAPIView.as_view(), name='project-list'),
    path("engagements/", EngagementListAPIView.as_view(), name='engagement-list')
]