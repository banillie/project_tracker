from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import (
    engagement_list_view,
    engagement_detail_view,
    engagement_delete_view,
    EngagementUpdateView,
    engagement_create_view,
    engagement_create_project_hx_view,
)

app_name = "engagements"
urlpatterns = [
    path("", engagement_list_view, name="engagement-list"),
    path("create/", engagement_create_view, name="engagement-create"),
    path("<int:id>/", engagement_detail_view, name="engagement-detail"),
    path("<int:id>/delete/", engagement_delete_view, name="engagement-delete"),
    path("<int:id>/update/", login_required(EngagementUpdateView.as_view()), name="engagement-update"),
    path("create-new-project/", engagement_create_project_hx_view, name="hx-project-create")
]
