"""project_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based viewshttp://127.0.0.1:8000/

    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

from engagements.views import engagement_list_view, engagement_create_view, engagement_detail_view
from pages.views import home_view


urlpatterns = [
    path("projects/", include("projects.urls")),
    path("stakeholders/", include("stakeholders.urls")),
    path("ppdds/", include("ppdds.urls")),
    # path("engagements/", include("engagements.urls")),
    path("engagements/", engagement_list_view, name="engagement-list"),
    path("engagements/create/", engagement_create_view, name="engagement-create"),
    path("engagements/<int:id>/", engagement_detail_view, name="engagement-detail"),

    path("", home_view, name="home"),
    path("admin/", admin.site.urls),
]
