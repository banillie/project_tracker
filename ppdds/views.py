from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from .forms import PPDDForm

from .models import PPDD
from engagements.models import Engagement
from projects.models import Project


@login_required
def ppdds_create_view(request):
    form = PPDDForm(request.POST or None)
    context = {
        'form': form,
    }
    # if form.is_valid():
    #     form.save()
    #     form = PPDDForm()
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        return redirect(obj.get_absolute_url())
    return render(request, "ppdds/create-update.html", context)



@login_required
def ppdds_update_view(request, slug=None):
    obj = get_object_or_404(PPDD, slug=slug)
    form = PPDDForm(request.POST or None, instance=obj)
    context = {
        'form': form,
        # 'object': obj,
    }
    if form.is_valid():
        form.save()
        return redirect('../')
        # context['message'] = 'Date Saved'
    # if request.htmx:
    #     return render(request, "ppdds/partials/forms.html", context)
    return render(request, "ppdds/create-update.html", context)



@login_required
def ppdds_detail_view(request, slug):
    obj = get_object_or_404(PPDD, slug=slug)
    # qs = Engagement.objects.filter(ppdds__slug=slug)
    # context = {
    #     "object": obj,
    #     "engagement_list": qs,
    # }
    engage_qs = Engagement.objects.filter(ppdds__slug=slug)
    project_qs = []
    for x in engage_qs.all().values('projects').distinct():
        project_qs.append(Project.objects.get(pk=x['projects']))
    context = {
        "object": obj,
        "engagement_list": engage_qs,
        "project_list": project_qs,
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


