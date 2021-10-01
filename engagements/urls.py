from django.urls import path
from .views import (
    engagement_create_view,
    engagement_list_view,
    engagement_detail_view,
    engagement_delete_view,
    engagement_update_view,
    EngagementCreateView
)

app_name = "engagements"
urlpatterns = [
    path("", engagement_list_view, name="engagement-list"),
    path("test/", EngagementCreateView.as_view(), name='engagement-test'),
    path("create/", engagement_create_view, name="engagement-create"),
    path("<int:id>/", engagement_detail_view, name="engagement-detail"),
    path("<int:id>/delete/", engagement_delete_view, name="engagement-delete"),
    path("<int:id>/update/", engagement_update_view, name="engagement-create"),
]
