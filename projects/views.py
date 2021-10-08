# Create your views here. Everything related to projects app should be here.
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProjectForm
from .models import Project


@login_required
def project_list_view(request):
    queryset = Project.objects.all().order_by('name')
    context = {
        "object_list": queryset
    }
    return render(request, "projects/project_list.html", context)


@login_required
def project_delete_view(request, id):
    obj = get_object_or_404(Project, id=id)  # handles page not found.
    if request.method == "POST":
        obj.delete()  # confirming delete
        return redirect('../../')
    context = {
        "object": obj,
    }
    return render(request, "projects/project_delete.html", context)


@login_required
def project_detail_view(request, id):
    obj = get_object_or_404(Project, id=id)  # handles page not found.
    context = {
        "object": obj,
    }
    return render(request, "projects/project_detail.html", context)


@login_required
def project_search_view(request):
    # print(request)
    query_dict = request.GET
    # print(query_dict)
    query = query_dict.get("query")
    obj = None
    if query is not None:
        obj = Project.objects.get(id=query)
    context = {
        "object": obj,
    }
    return render(request, "projects/project_search.html", context)


@login_required
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


@login_required
def project_create_view(request):
    form = ProjectForm(request.POST or None)
    context = {
        'form': form,
    }
    if form.is_valid():
        project_object = form.save()
        context['form'] = ProjectForm()
        context['object'] = project_object
        context['created'] = True
    return render(request, "projects/project_create.html", context)


