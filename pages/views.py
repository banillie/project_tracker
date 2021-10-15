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
    query = request.GET.get('query')
    print(query)
    qs = Project.objects.search(query=query)
    context = {
        "object_list": qs,
    }
    return render(request, "search.html", context)





