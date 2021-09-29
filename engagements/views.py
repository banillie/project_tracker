from django.shortcuts import render, get_object_or_404, redirect
from .forms import EngagementForm


def engagement_create_view(request):
    form = EngagementForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = EngagementForm()
    context = {
        'form': form,
    }
    return render(request, "engagements/engagement_create.html", context)