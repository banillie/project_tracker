from django.urls import path

from . import views

from projects.views import ProjectListAPIView

urlpatterns = [
    # path('', views.api_home),
    path("projects/", ProjectListAPIView.as_view(), name='project-list'),
]