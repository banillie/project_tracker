import datetime
import os

from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from django.conf import settings
from projects.models import Project
from stakeholders.models import Stakeholder
from ppdds.models import PPDD
from engagements.models import Engagement

from data_wraggling.upload import excel_download


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


# @user_passes_test(lambda u: u.is_superuser)  # only for super users removing for now.
def download_master(request):
    today = datetime.date.today()
    file_name = f"engagement_tracker_master_{today}.xlsx"
    save_path = os.path.join(settings.MEDIA_ROOT, 'downloads', file_name)  # need to create media root
    excel_download(save_path)
    with open(save_path, "rb") as excel:
        data = excel.read()
        response = HttpResponse(data, content_type="application/vnd.ms-excel")  # what's content type
        response["Content-Disposition"] = f"attachment; filename={file_name}"
        return response
