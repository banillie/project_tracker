from django.urls import path
from .views import (
    engagement_create_view,
    engagement_list_view,
    engagement_detail_view,
)

# app_name = "engagements"
# urlpatterns = [
#     path("engagements/", engagement_list_view, name="engagement-list"),
#     path("create/", engagement_create_view, name="engagement-create"),
#     path("<int:id>/", engagement_detail_view, name="engagement-detail"),
#     path("<int:id>/delete/", ppdds_delete_view, name="ppdd-delete"),
#     path("<int:id>/update/", ppdds_update_view, name="ppdd-create"),
# ]
