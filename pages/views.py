from itertools import chain

from django.http import HttpResponse
from django.shortcuts import render
from projects.models import Project
from stakeholders.models import Stakeholder
from ppdds.models import PPDD


def home_view(request, *args, **kwargs):
    # print(request.user)
    my_context = {
        "my_text": "The purpose of the tracker is to...",
    }
    return render(request, "home.html", my_context)


def search_view(request):
    if request.method == "POST":
        query = request.POST['searched']
        project_qs = Project.objects.search(query=query)
        stakeholder_qs = Stakeholder.objects.search(query=query)
        ppdd_qs = PPDD.objects.search(query=query)
        context = {
            "searched": query,
            "project_model_search": project_qs,
            "stakeholder_model_search": stakeholder_qs,
            "ppdd_model_search": ppdd_qs
        }
        return render(request, "search.html", context)
    else:
        return render(request, "search.html", {})
