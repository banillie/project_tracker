from django.urls import path
from .views import (
    stakeholders_detail_view,
    stakeholders_create_view,
    stakeholder_delete_view,
    stakeholder_list_view,
    stakeholder_update_view,
)

app_name = "stakeholders"
urlpatterns = [
    path("", stakeholder_list_view, name="stakeholder-list"),
    path("create/", stakeholders_create_view, name="stakeholder-create"),
    path("<int:id>/", stakeholders_detail_view, name="stakeholder-detail"),
    path("<int:id>/delete/", stakeholder_delete_view, name="stakeholder-delete"),
    path("<int:id>/update/", stakeholder_update_view, name="stakeholder-create"),
]
