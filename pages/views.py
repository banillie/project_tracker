from django.http import HttpResponse
from django.shortcuts import render


def home_view(request, *args, **kwargs):
    # print(request.user)
    # return HttpResponse("<h1>Hello World</h1>")
    my_context = {
        "my_text": "This is a project",
    }
    return render(request, "home.html", my_context)


def project_view(request, *args, **kwargs):
    print(request.user)
    my_context = {
        "my_text": "This is a project",
        "project_name": "Project Django",
        "my_list": [12, 4, 5, 78, "nice", True],
        "html": "<h1>Hello World</h1>"
    }
    return render(request, "project.html", my_context)
    # return HttpResponse("<h1>Contact Page</h1>")
