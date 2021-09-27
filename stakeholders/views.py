from django.shortcuts import render

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


def stakeholders_detail_view(request):
    obj = Stakeholder.objects.get(id=1)
    print(obj.last_name)
    context = {
        'object': obj,
    }
    return render(request, "stakeholders/stakeholder_detail.html", context)
