from django.http import HttpResponse
from django.shortcuts import render


def home_view(request, *args, **kwargs):
    # print(request.user)
    my_context = {
        "my_text": "The purpose of the tracker is to...",
    }
    return render(request, "home.html", my_context)


def stakeholder_view(request, *args, **kwargs):
    my_context = {
        "my_text": "Stakeholders stakeholders stakeholders",
        "my_number": 636257,
    }
    return render(request, "stakeholder.html", my_context)


