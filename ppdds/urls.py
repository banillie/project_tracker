from django.urls import path
from .views import (
    ppdds_list_view,
    ppdds_delete_view,
    ppdds_create_view,
    ppdds_detail_view,
    ppdds_update_view,
)

app_name = "ppdds"
urlpatterns = [
    path("", ppdds_list_view, name="list"),
    path("create/", ppdds_create_view, name="create"),
    path("<slug:slug>/delete/", ppdds_delete_view, name="delete"),
    path("<slug:slug>/update/", ppdds_update_view, name="update"),
    path("<slug:slug>/", ppdds_detail_view, name="detail"),
]
