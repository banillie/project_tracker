import operator

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse
from django.http import Http404
from .forms import PPDDForm

from .models import PPDD
from engagements.models import Engagement
from projects.models import Project


@login_required
def ppdds_create_view(request):
    if not request.htmx:
        return Http404

    ppdd_form = PPDDForm(request.POST or None)
    context = {
        "hx_create_ppdd_url_list": reverse("ppdds:create"),
        "ppdd_form": ppdd_form,
    }
    if ppdd_form.is_valid():
        ppdd_form.save()
        queryset = PPDD.objects.all().order_by('last_name')
        context["object_list"] = queryset
        return render(request, "ppdds/partials/hx_create_ppdd_in_ppdd.html", context)
    return render(request, "engagements/partials/hx_create_ppdd_modal_form.html", context)
    #
    # form = PPDDForm(request.POST or None)
    # error_msg = None
    # if form.is_valid():
    #     obj = form.save(commit=False)
    #     obj.user = request.user
    #     try:
    #         obj.save()
    #         return redirect(obj.get_absolute_url())
    #     except IntegrityError:  # slug field set to unique
    #         error_msg = 'PPDD colleague already exists'
    # context = {
    #     'form': form,
    #     'error_msg': error_msg
    # }
    # return render(request, "ppdds/create-update.html", context)


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
    engage_qs = Engagement.objects.filter(ppdds__slug=slug).order_by('-date')
    project_qs = []
    for x in engage_qs.all().values('projects').distinct():
        try:
            p = Project.objects.get(pk=x['projects'])
            if p not in project_qs:  # remove repeats
                project_qs.append(p)
        except ObjectDoesNotExist:
            pass
    project_qs_ordered = sorted(project_qs, key=operator.attrgetter('name'))
    context = {
        "object": obj,
        "engagement_list": engage_qs,
        "project_list": project_qs_ordered,
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
        "object_list": queryset,
        "hx_create_ppdd_url_list": reverse("ppdds:create"),
    }
    return render(request, "ppdds/list.html", context)
