from django.http import HttpResponse
from django.shortcuts import render


def home_view(request, *args, **kwargs):
    # print(request.user)
    my_context = {
        "my_text": "The purpose of the tracker is to...",
    }
    return render(request, "home.html", my_context)





