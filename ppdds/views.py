from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from .forms import PPDDForm

from .models import PPDD


@login_required
def ppdds_create_view(request):
    form = PPDDForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = PPDDForm()
    context = {
        'form': form,
    }
    return render(request, "ppdds/ppdd_create.html", context)


@login_required
def ppdds_update_view(request, id):
    obj = get_object_or_404(PPDD, id=id)  # handles page not found.
    form = PPDDForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('../')
    context = {
        'form': form
    }
    return render(request, "ppdds/ppdd_create.html", context)


@login_required
def ppdds_detail_view(request, id):
    obj = get_object_or_404(PPDD, id=id)
    context = {
        "object": obj
    }
    return render(request, "ppdds/ppdd_detail.html", context)


@login_required
def ppdds_delete_view(request, id):
    obj = get_object_or_404(PPDD, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect('../../')
    context = {
        "object": obj
    }
    return render(request, "ppdds/ppdd_delete.html", context)


@login_required
def ppdds_list_view(request):
    queryset = PPDD.objects.all().order_by('last_name')
    context = {
        "object_list": queryset
    }
    return render(request, "ppdds/ppdd_list.html", context)


