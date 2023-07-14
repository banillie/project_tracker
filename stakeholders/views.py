import operator

from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.urls import reverse

from projects.models import Project
from .forms import StakeholderForm

from .models import Stakeholder
from engagements.models import Engagement


@login_required
def stakeholders_create_view(request, slug=None):
    if not request.htmx:
        return Http404

    if not slug:
        stakeholder_form = StakeholderForm(request.POST or None)
    else:
        obj = get_object_or_404(Stakeholder, slug=slug)  # handles page not found.
        stakeholder_form = StakeholderForm(request.POST or None, instance=obj)

    context = {
        "stakeholder_form": stakeholder_form,
    }
    if not slug:
        context["hx_create_stakeholder_url_list"] = reverse("stakeholders:create")
    else:
        context["hx_update_stakeholder_url"] = obj.get_update_url

    if stakeholder_form.is_valid():
        stakeholder_form.save()
        if not slug:
            queryset = Stakeholder.objects.all().order_by("last_name")
            context["object_list"] = queryset
            return render(
                request,
                "stakeholders/partials/hx_create_stakeholder_in_stakeholder_list.html",
                context,
            )
        else:
            context["object"] = obj
            return render(
                request,
                "stakeholders/partials/hx_update_stakeholder.html",
                context,
            )
    return render(
        request, "engagements/partials/hx_create_stakeholder_modal_form.html", context
    )

    # form = StakeholderForm(request.POST or None)
    # error_msg = None
    # if form.is_valid():
    #     obj = form.save(commit=False)
    #     obj.user = request.user
    #     try:
    #         obj.save()
    #         return redirect(obj.get_absolute_url())
    #     except IntegrityError:  # slug field set to unique
    #         error_msg = 'Stakeholder already exists'
    # context = {
    #     'form': form,
    #     'error_msg': error_msg,
    # }
    # return render(request, "stakeholders/create.html", context)


# @login_required
# def stakeholder_update_view(request, slug):
# form = StakeholderForm(request.POST or None, instance=obj)
# if form.is_valid():
#     form.save()
#     return redirect('../')
# context = {
#     'form': form
# }
# return render(request, "stakeholders/create.html", context)
#

@login_required
def stakeholders_detail_view(request, slug):
    obj = get_object_or_404(Stakeholder, slug=slug)
    engagement_qs = Engagement.objects.filter(stakeholders__slug=slug).order_by("-date")

    project_ids = engagement_qs.values_list("projects", flat=True).distinct()
    project_list = Project.objects.filter(pk__in=project_ids).order_by("name")

    context = {
        "object": obj,
        "engagement_list": engagement_qs,
        "project_list": project_list,
        "hx_update_stakeholder_url": obj.get_update_url,
    }
    return render(request, "stakeholders/detail.html", context)


# @login_required
# def stakeholders_detail_view(request, slug):
#     obj = get_object_or_404(Stakeholder, slug=slug)
#     engage_qs = Engagement.objects.filter(stakeholders__slug=slug).order_by("-date")
#     project_qs = []
#     for x in engage_qs.all().values("projects").distinct():
#         try:
#             p = Project.objects.get(pk=x["projects"])
#             if p not in project_qs:  # remove repeats
#                 project_qs.append(p)
#         except ObjectDoesNotExist:
#             pass
#     project_qs_ordered = sorted(project_qs, key=operator.attrgetter("name"))
#     context = {
#         "object": obj,
#         "engagement_list": engage_qs,
#         "project_list": project_qs_ordered,
#         "hx_update_stakeholder_url": obj.get_update_url,
#     }
#     return render(request, "stakeholders/detail.html", context)


@login_required
def stakeholder_delete_view(request, slug):
    obj = get_object_or_404(Stakeholder, slug=slug)
    if request.method == "POST":
        obj.delete()
        return redirect("../../")
    context = {"object": obj}
    return render(request, "stakeholders/delete.html", context)


@login_required
def stakeholder_list_view(request):
    queryset = Stakeholder.objects.all().order_by("last_name")
    context = {
        "object_list": queryset,
        "hx_create_stakeholder_url_list": reverse("stakeholders:create"),
    }
    return render(request, "stakeholders/list.html", context)
