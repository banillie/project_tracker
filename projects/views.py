# Create your views here. Everything related to projects app should be here.
from django.shortcuts import render, get_object_or_404, redirect
from .forms import ProjectForm
from .models import Project


def project_list_view(request):
    queryset = Project.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, "projects/project_list.html", context)


def project_delete_view(request, id):
    obj = get_object_or_404(Project, id=id)  # handles page not found.
    if request.method == "POST":
        obj.delete()  # confirming delete
        return redirect('../../')
    context = {
        "object": obj,
    }
    return render(request, "projects/project_delete.html", context)


def project_detail_view(request, id):
    obj = get_object_or_404(Project, id=id)  # handles page not found.
    context = {
        "object": obj,
    }
    return render(request, "projects/project_detail.html", context)


def project_update_view(request, id):
    obj = get_object_or_404(Project, id=id)  # handles page not found.
    form = ProjectForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('../')
    context = {
        'form': form
    }
    return render(request, "projects/project_create.html", context)


def project_create_view(request):
    form = ProjectForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProjectForm()
    context = {
        'form': form,
    }
    return render(request, "projects/project_create.html", context)

