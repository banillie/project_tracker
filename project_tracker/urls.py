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
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path

from accounts.views import login_view, logout_view, register_view
from pages.views import home_view, search_view, download_master, download_view, mi_view


urlpatterns = [
    path("", home_view, name="home"),

    path("api/", include("api.urls")),
    path("api/projects/", include('projects.urls')),

    path("projects/", include("projects.urls")),
    path("stakeholders/", include("stakeholders.urls")),
    path("ppdds/", include("ppdds.urls")),
    path("engagements/", include("engagements.urls")),
    path("download/", download_view, name="download"),
    path("download_master/", download_master, name="download_master"),
    path("mi/", mi_view, name='mi'),
    path("admin/", admin.site.urls),
    path("login/", login_view),
    path("logout/", logout_view),
    path("register/", register_view),
    # path("hx/search/", hx_search_view),
    path("search/", search_view, name="search"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
