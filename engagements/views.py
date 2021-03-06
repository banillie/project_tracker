from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required

from rest_framework import generics

from easy_select2 import select2_modelform
from .models import Engagement, EngagementTopic
from .forms import EngagementForm
from .serializers import EngagementSerializer, EngagementTopicSerializer


class EngagementListAPIView(generics.ListAPIView):
    queryset = Engagement.objects.all()
    serializer_class = EngagementSerializer


class EngagementTopicListAPIView(generics.ListAPIView):
    queryset = EngagementTopic.objects.all()
    serializer_class = EngagementTopicSerializer


# @login_required
# def engagement_create_view(request):
#     form = EngagementForm(request.POST or None)
#     context = {
#         'form': form,
#     }
#     if form.is_valid():
#         obj = form.save(commit=False)
#         obj.user = request.user
#         obj.save()
#         return redirect(obj.get_absolute_url())
#     return render(request, "engagements/engagement_create.html", context)


class EngagementCreateView(CreateView):
    model = Engagement
    form_class = EngagementForm
    # form_class = select2_modelform(Engagement, attrs={'width': '100%'})
    # form_class = select2_modelform(Engagement, attrs={'class': 'form-control'})
    # success_url = reverse_lazy('engagement-form')
    template_name = "engagements/engagement_create.html"

    def form_valid(self, form):
        # return super().form_valid(form)
        form.instance.user = self.request.user
        form.save()
        return super(EngagementCreateView, self).form_valid(form)


class EngagementUpdateView(UpdateView):
    model = Engagement
    form_class = EngagementForm
    # form_class = select2_modelform(Engagement, attrs={'width': '100%'})
    # success_url = reverse_lazy('engagement-form')
    template_name = "engagements/engagement_create.html"

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Engagement, id=id_)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


# @login_required
# def engagement_create_view(request):
#     form = EngagementForm(request.POST or None)
#     # form = EngagementForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         form = EngagementForm()
#     context = {
#         'form': form,
#     }
#     return render(request, "engagements/engagement_create.html", context)


@login_required
def engagement_list_view(request):
    queryset = Engagement.objects.all().order_by('-date')  # reverse order
    # print(queryset.all())
    context = {
        "object_list": queryset
    }
    return render(request, "engagements/engagement_list.html", context)


@login_required
def engagement_detail_view(request, id):
    obj = get_object_or_404(Engagement, id=id)
    project_queryset = obj.projects.get_queryset()
    stakeholder_queryset = obj.stakeholders.get_queryset()
    ppdd_queryset = obj.ppdds.get_queryset()
    topic_queryset = obj.topics.get_queryset()
    # type_queryset = obj.engagement_types.get_queryset()
    # ws_queryset = obj.engagement_workstreams.get_queryset()
    context = {
        "object": obj,
        "project_list": project_queryset,
        "stakeholder_list": stakeholder_queryset,
        "ppdd_list": ppdd_queryset,
        "topic_list": topic_queryset,
    }
    return render(request, "engagements/engagement_detail.html", context)


# @login_required
# def engagement_update_view(request, id):
#     obj = get_object_or_404(Engagement, id=id)
#     form = EngagementForm(request.POST or None, instance=obj)
#     if form.is_valid():
#         form.save()
#         # form.save_m2m()
#         return redirect('../')
#     context = {
#         'form': form
#     }
#     return render(request, "engagements/engagement_create.html", context)


def engagement_delete_view(request, id):
    obj = get_object_or_404(Engagement, id=id)
    queryset = obj.projects.get_queryset()
    if request.method == "POST":
        obj.delete()
        return redirect('../../')
    context = {
        "object": obj,
        "object_list": queryset
    }
    return render(request, "engagements/engagement_delete.html", context)


