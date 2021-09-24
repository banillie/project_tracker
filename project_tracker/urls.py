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

from pages.views import home_view, project_view

urlpatterns = [
    path("projects/", include('projects.urls')),
    path("", home_view, name="home"),
    # path("project/", project_view, name="project"),
    # path("detail/", project_detail_view),


    path("admin/", admin.site.urls),
]
