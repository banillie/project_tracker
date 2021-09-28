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
    path("", ppdds_list_view, name="ppdd-list"),
    path("create/", ppdds_create_view, name="ppdd-create"),
    path("<int:id>/", ppdds_detail_view, name="ppdd-detail"),
    path("<int:id>/delete/", ppdds_delete_view, name="ppdd-delete"),
    path("<int:id>/update/", ppdds_update_view, name="ppdd-create"),
]
