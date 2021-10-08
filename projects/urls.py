from django.urls import path
from .views import (
    project_detail_view,
    project_create_view,
    project_update_view,
    project_delete_view,
    project_list_view,
    project_search_view,
)

app_name = 'projects'
urlpatterns = [
    path("", project_list_view, name='project-list'),
    path("search/", project_search_view, name='project_search'),
    path("create/", project_create_view, name='project-create'),
    path("<int:id>/", project_detail_view, name='project-detail'),
    path("<int:id>/update/", project_update_view, name='project-create'),
    path("<int:id>/delete/", project_delete_view, name='project-delete'),
]
