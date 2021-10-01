from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView
from django.views.generic.edit import CreateView
from easy_select2 import select2_modelform
from .forms import EngagementForm
from .models import Engagement


class EngagementCreateView(CreateView):
    model = Engagement
    form_class = select2_modelform(Engagement)
    success_url = reverse_lazy('engagement-test')


def engagement_create_view(request):
    form = EngagementForm(request.POST or None)
    # form = EngagementForm(request.POST or None)
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
    queryset = obj.projects.get_queryset()
    context = {
        "object": obj,
        "object_list": queryset,
    }
    return render(request, "engagements/engagement_detail.html", context)


def engagement_update_view(request, id):
    obj = get_object_or_404(Engagement, id=id)
    form = EngagementForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        # form.save_m2m()
        return redirect('../')
    context = {
        'form': form
    }
    return render(request, "engagements/engagement_create.html", context)


def engagement_delete_view(request, id):
    obj = get_object_or_404(Engagement, id=id)
    queryset = obj.projects.get_queryset()
    if request.method == "POST":
        obj.delete()
        return redirect('../../')
    context = {
        "object": obj,
        "object_list": queryset
    }
    return render(request, "engagements/engagement_delete.html", context)