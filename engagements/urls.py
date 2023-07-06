from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import (
    engagement_list_view,
    engagement_detail_view,
    engagement_delete_view,
    engagement_create_update_view,
    engagement_create_project_hx_view,
    engagement_create_stakeholder_hx_view,
)

app_name = "engagements"
urlpatterns = [
    path("", engagement_list_view, name="engagement-list"),
    path("create/", engagement_create_update_view, name="engagement-create"),
    path("<int:id>/", engagement_detail_view, name="engagement-detail"),
    path("<int:id>/delete/", engagement_delete_view, name="engagement-delete"),
    path("<int:id>/update/", engagement_create_update_view, name="engagement-update"),
    path(
        "create-new-project/",
        engagement_create_project_hx_view,
        name="hx-project-create",
    ),
    path(
        "create-new-stakeholder/",
        engagement_create_stakeholder_hx_view,
        name="hx-stakeholder-create",
    ),
]
