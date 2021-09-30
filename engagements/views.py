from django.shortcuts import render, get_object_or_404, redirect
from .forms import EngagementForm
from .models import Engagement


def engagement_create_view(request):
    form = EngagementForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = EngagementForm()
    context = {
        'form': form,
    }
    return render(request, "engagements/engagement_create.html", context)


def engagement_list_view(request):
    queryset = Engagement.objects.all()
    # print(queryset.all())
    context = {
        "object_list": queryset
    }
    return render(request, "engagements/engagement_list.html", context)


def engagement_detail_view(request, id):
    obj = get_object_or_404(Engagement, id=id)
    context = {
        "object": obj
    }
    return render(request, "engagements/engagement_detail.html", context)


def engagement_update_view(request, id):
    obj = get_object_or_404(Engagement, id=id)
    form = EngagementForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('../')
    context = {
        'form': form
    }
    return render(request, "engagements/engagement_create.html", context)


def engagement_delete_view(request, id):
    obj = get_object_or_404(Engagement, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect('../../')
    context = {
        "object": obj
    }
    return render(request, "engagements/engagement_delete.html", context)