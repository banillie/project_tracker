from django.shortcuts import render, get_object_or_404, redirect

from .forms import StakeholderForm

from .models import Stakeholder


def stakeholders_create_view(request):
    form = StakeholderForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = StakeholderForm()
    context = {
        'form': form,
    }
    return render(request, "stakeholders/stakeholder_create.html", context)


def stakeholder_update_view(request, id):
    obj = get_object_or_404(Stakeholder, id=id)  # handles page not found.
    form = StakeholderForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('../')
    context = {
        'form': form
    }
    return render(request, "stakeholders/stakeholder_create.html", context)


def stakeholders_detail_view(request, id):
    obj = get_object_or_404(Stakeholder, id=id)
    context = {
        "object": obj
    }
    return render(request, "stakeholders/stakeholder_detail.html", context)


def stakeholder_delete_view(request, id):
    obj = get_object_or_404(Stakeholder, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect('../../')
    context = {
        "object": obj
    }
    return render(request, "stakeholders/stakeholder_delete.html", context)


def stakeholder_list_view(request):
    queryset = Stakeholder.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, "stakeholders/stakeholder_list.html", context)