from django.urls import path
from .views import (
    engagement_create_view,
)

app_name = "engagements"
urlpatterns = [
    # path("", ppdds_list_view, name="ppdd-list"),
    path("create/", engagement_create_view, name="engagement-create"),
    # path("<int:id>/", ppdds_detail_view, name="ppdd-detail"),
    # path("<int:id>/delete/", ppdds_delete_view, name="ppdd-delete"),
    # path("<int:id>/update/", ppdds_update_view, name="ppdd-create"),
]
