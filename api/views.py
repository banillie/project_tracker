from django.http import JsonResponse

from projects.models import Project


def api_home(request, *args, **kwargs):
    model_data = Project.objects.all().order_by("?").first()
    data = {'title': model_data.name}
    return JsonResponse(data)

