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
    path("", stakeholder_list_view, name="list"),
    path("create/", stakeholders_create_view, name="create"),
    path("<slug:slug>/delete/", stakeholder_delete_view, name="delete"),
    path("<slug:slug>/update/", stakeholder_update_view, name="update"),
    path("<slug:slug>/", stakeholders_detail_view, name="detail"),
]
