import datetime
import os
import tempfile

from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import login_required
from django.conf import settings
from projects.models import Project
from stakeholders.models import Stakeholder
from ppdds.models import PPDD
from engagements.models import Engagement

from data_wraggling.upload import excel_download_pbi


def home_view(request, *args, **kwargs):
    # print(request.user)
    my_context = {
        "my_text": "Welcome to the home page for the PPDD Project Tracker Tool.",
    }
    return render(request, "home.html", my_context)


def search_view(request):
    if request.method == "POST":
        query = request.POST['searched']
        project_qs = Project.objects.search(query=query)
        stakeholder_qs = Stakeholder.objects.search(query=query)
        ppdd_qs = PPDD.objects.search(query=query)
        # engagement_qs = Engagement.objects.search(query=query)
        context = {
            "searched": query,
            "project_model_search": project_qs,
            "stakeholder_model_search": stakeholder_qs,
            "ppdd_model_search": ppdd_qs,
            # "engagement_model_search": engagement_qs,
        }
        return render(request, "search.html", context)
    else:
        return render(request, "search.html", {})


@login_required
def download_view(request, *args, **kwargs):
    return render(request, "download.html")


# @user_passes_test(lambda u: u.is_superuser)
# @login_required
# def download_master(request):
#     today = datetime.date.today()
#     file_name = f"engagement_tracker_master_{today}.xlsx"
#     # save_path = os.path.join(settings.MEDIA_ROOT, 'downloads', file_name)  # not using media root.
#     with tempfile.TemporaryDirectory() as tmpdir:
#         save_path = os.path.join(tmpdir, file_name)
#         excel_download(save_path)
#         with open(save_path, "rb") as excel:
#             data = excel.read()
#             response = HttpResponse(data, content_type="application/vnd.ms-excel")
#             response["Content-Disposition"] = f"attachment; filename={file_name}"
#             return response

@login_required
def download_master(request):
    today = datetime.date.today()
    file_name = f"ppdd_engagement_tracker_pbi_data_{today}.xlsx"
    # save_path = os.path.join(settings.MEDIA_ROOT, 'downloads', file_name)  # not using media root.
    with tempfile.TemporaryDirectory() as tmpdir:
        save_path = os.path.join(tmpdir, file_name)
        excel_download_pbi(save_path)
        with open(save_path, "rb") as excel:
            data = excel.read()
            response = HttpResponse(data, content_type="application/vnd.ms-excel")
            response["Content-Disposition"] = f"attachment; filename={file_name}"
            return response