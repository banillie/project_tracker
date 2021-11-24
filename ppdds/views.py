from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from .forms import PPDDForm

from .models import PPDD
from engagements.models import Engagement


@login_required
def ppdds_create_view(request):
    form = PPDDForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = PPDDForm()
    context = {
        'form': form,
    }
    return render(request, "ppdds/create-update.html", context)


@login_required
def ppdds_update_view(request, slug=None):
    obj = get_object_or_404(PPDD, slug=slug)
    form = PPDDForm(request.POST or None, instance=obj)
    context = {
        'form': form,
        'object': obj,
    }
    if form.is_valid():
        form.save()
        # context['message'] = 'Date Saved'
    # if request.htmx:
    #     return render(request, "ppdds/partials/forms.html", context)
    return render(request, "ppdds/create-update.html", context)


@login_required
def ppdds_detail_view(request, slug):
    obj = get_object_or_404(PPDD, slug=slug)
    qs = Engagement.objects.filter(ppdds__slug=slug)
    context = {
        "object": obj,
        "engagement_list": qs,
    }
    return render(request, "ppdds/detail.html", context)


@login_required
def ppdds_delete_view(request, slug):
    obj = get_object_or_404(PPDD, slug=slug)
    if request.method == "POST":
        obj.delete()
        return redirect('../../')
    context = {
        "object": obj
    }
    return render(request, "ppdds/delete.html", context)


@login_required
def ppdds_list_view(request):
    queryset = PPDD.objects.all().order_by('last_name')
    context = {
        "object_list": queryset
    }
    return render(request, "ppdds/list.html", context)


