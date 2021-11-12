from itertools import chain

from django.http import HttpResponse
from django.shortcuts import render
from projects.models import Project


def home_view(request, *args, **kwargs):
    # print(request.user)
    my_context = {
        "my_text": "The purpose of the tracker is to...",
    }
    return render(request, "home.html", my_context)


def search_view(request):
    if request.method == "POST":
        query = request.POST['searched']
        qs = Project.objects.search(query=query)
        context = {
            "searched": query,
            "search_object_list": qs,
        }
        return render(request, "search.html", context)
    else:
        return render(request, "search.html", {})
