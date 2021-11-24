from django.urls import path
from .views import (
    project_detail_view,
    # project_detail_hx_view,
    project_create_view,
    project_update_view,
    project_delete_view,
    project_list_view,
    project_search_view,
)

app_name = 'projects'
urlpatterns = [
    path("", project_list_view, name='list'),
    # path("search/", project_search_view, name='search'),
    path("create/", project_create_view, name='create'),
    # path("hx/<slug:slug>/", project_detail_hx_view, name='hx-detail'),
    path("<slug:slug>/update/", project_update_view, name='update'),
    path("<slug:slug>/delete/", project_delete_view, name='delete'),
    path("<slug:slug>/", project_detail_view, name='detail'),
]
