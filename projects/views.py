from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import ProjectForm
from .models import Project


@login_required
def project_list_view(request):
    queryset = Project.objects.all().order_by('name')
    context = {
        "object_list": queryset
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
def project_detail_view(request, slug=None):
    hx_url = reverse("projects:hx-detail", kwargs={"slug": slug})
    # print(hx_url)
    context = {
        "hx_url": hx_url,
    }
    return render(request, "projects/detail.html", context)


@login_required
def project_detail_hx_view(request, slug=None):
    try:
        obj = Project.objects.get(slug=slug)
    except:
        obj = None
    if obj is None:
        return HttpResponse("Not found.")
    context = {
        "object": obj,
    }
    return render(request, "projects/partials/detail.html", context)



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
        'object': obj,
    }
    if form.is_valid():
        form.save()
        context['message'] = 'Date Saved'
    if request.htmx:
        return render(request, "projects/partials/forms.html", context)
    return render(request, "projects/create-update.html", context)


@login_required
def project_create_view(request):
    form = ProjectForm(request.POST or None)
    context = {
        'form': form,
    }
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        return redirect(obj.get_absolute_url())
    return render(request, "projects/create-update.html", context)


