import operator

from django.urls import reverse
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError

from rest_framework import generics

from engagements.models import Engagement
from stakeholders.models import Stakeholder
from .forms import ProjectForm
from .models import Project
from .serializers import ProjectSerializer


class ProjectDetailAPIView(generics.RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    # lookup_field = 'pk'


class ProjectListAPIView(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


@login_required
def project_list_view(request):
    queryset = Project.objects.all().order_by('name')
    context = {
        "object_list": queryset,
        "hx_create_project_url_list": reverse("projects:create"),
    }
    return render(request, "projects/list.html", context)


@login_required
def project_delete_view(request, slug):
    obj = get_object_or_404(Project, slug=slug)  # handles page not found.
    if request.method == "POST":
        obj.delete()  # confirming delete
        return redirect('../../')
    context = {
        "object": obj,
    }
    return render(request, "projects/delete.html", context)


@login_required
def project_detail_view(request, slug):
    obj = get_object_or_404(Project, slug=slug)
    engage_qs = Engagement.objects.filter(projects__slug=slug).order_by('-date')
    stake_qs = []
    for x in engage_qs.all().values('stakeholders').distinct():
        try:
            sh = Stakeholder.objects.get(pk=x['stakeholders'])
            if sh not in stake_qs:  # remove repeats
                stake_qs.append(sh)
        except ObjectDoesNotExist:
            pass
    stake_qs_ordered = sorted(stake_qs, key=operator.attrgetter('last_name'))
    context = {
        "object": obj,
        "engagement_list": engage_qs,
        "stakeholder_list": stake_qs_ordered,
    }
    return render(request, "projects/detail.html", context)


# @login_required
# def project_detail_hx_view(request, slug=None):
#     if not request.htmx:
#         raise Http404
#     try:
#         obj = Project.objects.get(slug=slug)
#     except:
#         obj = None
#     if obj is None:
#         return HttpResponse("Not found.")
#     engage_qs = Engagement.objects.filter(projects__slug=slug)
#     stake_qs = []
#     for x in engage_qs.all().values('stakeholders').distinct():
#         stake_qs.append(Stakeholder.objects.get(pk=x['stakeholders']))
#     context = {
#         "object": obj,
#         "engagement_list": engage_qs,
#         "stakeholder_list": stake_qs,
#     }
#     return render(request, "projects/partials/detail.html", context)


@login_required
def project_search_view(request):
    query = request.GET.get('query')
    qs = Project.objects.search(query=query)
    context = {
        "object_list": qs,
    }
    return render(request, "projects/search.html", context)


@login_required
def project_update_view(request, slug=None):
    obj = get_object_or_404(Project, slug=slug)
    form = ProjectForm(request.POST or None, instance=obj)
    context = {
        'form': form,
        # 'object': obj,
    }
    if form.is_valid():
        form.save()
        return redirect('../')
        # context['message'] = 'Date Saved'
    # if request.htmx:
    #     return render(request, "projects/partials/forms.html", context)
    return render(request, "projects/create-update.html", context)


@login_required
def project_create_view(request):
    if not request.htmx:
        return Http404

    project_form = ProjectForm(request.POST or None)
    context = {
        "hx_create_project_url_list": reverse("projects:create"),
        "project_form": project_form,
    }
    if project_form.is_valid():
        project_form.save()
        queryset = Project.objects.all().order_by('name')
        context = {
            "object_list": queryset,
            "hx_create_project_url_list": reverse("projects:create"),
        }
        return render(request, "projects/partials/hx_create_project_in_project_list.html", context)
    return render(request, "engagements/partials/hx_create_project_modal_form.html", context)

    # error_msg = None
    # if form.is_valid():
    #     obj = form.save(commit=False)
    #     obj.user = request.user
    #     try:
    #         obj.save()
    #         return redirect(obj.get_absolute_url())
    #     except IntegrityError:  # slug field set to unique
    #         error_msg = 'Project already exists'
    # context = {
    #     'form': form,
    #     'error_msg': error_msg,
    # }
    # return render(request, "projects/create-update.html", context)
    #






