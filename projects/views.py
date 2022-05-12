import operator

from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError

from rest_framework import generics, mixins, permissions

from engagements.models import Engagement
from stakeholders.models import Stakeholder
from .forms import ProjectForm
from .models import Project
from api.mixins import StaffEditorPermissionMixin, UserQuerySetMixin
from .serializers import ProjectSerializer


# permissions. new kind of permission based of user permissions.
# but also permission declared on view -> problematic.
# different types of permissions for each inherent view

class ProjectListCreateAPIView(
    # UserQuerySetMixin,
    StaffEditorPermissionMixin,
    generics.ListCreateAPIView,
):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    lookup_field = 'slug'

    # handled in settings
    # authentication_classes = [
    #     authentication.SessionAuthentication,
    #     TokenAuthentication,
    # ]
    #
    # permissions.IsAdminUser equates to staff and could also be used.
    # look at different permission classes
    # permission_classes = [
    #     permissions.IsAuthenticatedOrReadOnly,
    #     IsStaffEditorPermission,
    # ]

    # option to provide additional context in save
    # def perform_create(self, serializer):
    #     # serializer.save(user=self.request.user)
    #     print(serializer)
    #     serializer.save()
        # send a Django signal.

    # def get_queryset(self, *args, **kwargs):
    #     qs = super().get_queryset(*args, **kwargs)
    #     request = self.request
    #     user = request.user
    #     if not user.is_authenticated:
    #         return Project.objects.none()
    #     return qs.filter(user=user)


class ProjectDetailAPIView(
    StaffEditorPermissionMixin,
    generics.RetrieveAPIView
):
    queryset = Project.objects.all()
    # could change the Serializer to a DetailSerializer
    serializer_class = ProjectSerializer
    lookup_field = 'slug'

    # get queryset(): # custom qs


class ProjectUpdateAPIView(
    StaffEditorPermissionMixin,
    generics.UpdateAPIView
):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    lookup_field = "pk"

    def perform_update(self, serializer):
        instance = serializer.save()
        # option to do something similar to perform create?


class ProjectDestroyAPIView(
    StaffEditorPermissionMixin,
    generics.DestroyAPIView
):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    lookup_field = "pk"

    def perform_destroy(self, instance):
        super().perform_destroy(instance)


# did to learn about mixings.
# class ProjectMixinView(
#     mixins.CreateModelMixin,
#     mixins.ListModelMixin,  # provides ability to declare qs and serializer_class
#     mixins.RetrieveModelMixin,
#     generics.GenericAPIView,
# ):
#     queryset = Project.objects.all()
#     serializer_class = ProjectSerializer
#     lookup_field = "pk"
#
#     def get(self, request, *args, **kwargs):  # HTTP -> get
#         print(args, kwargs)
#         pk = kwargs.get("pk")
#         if pk is not None:
#             return self.retrieve(request, *args, **kwargs)
#         return self.list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)


@login_required
def project_list_view(request):
    queryset = Project.objects.all().order_by("name")
    context = {"object_list": queryset}
    # for instance in queryset:
    #     print(instance.get_absolute_url())
    return render(request, "projects/list.html", context)


@login_required
def project_delete_view(request, slug):
    obj = get_object_or_404(Project, slug=slug)  # handles page not found.
    if request.method == "POST":
        obj.delete()  # confirming delete
        return redirect("../../")
    context = {
        "object": obj,
    }
    return render(request, "projects/delete.html", context)


@login_required
def project_detail_view(request, slug):
    obj = get_object_or_404(Project, slug=slug)
    engage_qs = Engagement.objects.filter(projects__slug=slug).order_by("-date")
    stake_qs = []
    for x in engage_qs.all().values("stakeholders").distinct():
        try:
            stake_qs.append(Stakeholder.objects.get(pk=x["stakeholders"]))
        except ObjectDoesNotExist:
            pass
    stake_qs_ordered = list(
        set(sorted(stake_qs, key=operator.attrgetter("last_name")))
    )  # remove repeats
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
    query = request.GET.get("query")
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
        "form": form,
        # 'object': obj,
    }
    if form.is_valid():
        form.save()
        return redirect("../")
        # context['message'] = 'Date Saved'
    # if request.htmx:
    #     return render(request, "projects/partials/forms.html", context)
    return render(request, "projects/create-update.html", context)


@login_required
def project_create_view(request):
    form = ProjectForm(request.POST or None)
    # error_msg = None
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        # try:
        obj.save()
        return redirect(obj.get_absolute_url())
        # except IntegrityError:  # slug field set to unique
        #     error_msg = "Project already exists"
    context = {
        "form": form,
        # "error_msg": error_msg,
    }
    return render(request, "projects/create-update.html", context)
