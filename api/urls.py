from django.urls import path

from . import views

urlpatterns = [
    path('', views.api_home),  # localhost8000/api
]