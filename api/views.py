from django.http import JsonResponse
from django.forms.models import model_to_dict

from projects.models import Project


def api_home(request, *args, **kwargs):
    model_data = Project.objects.all().order_by("?").first()
    # data = {}
    data = model_to_dict(model_data, fields=['id'])
    return JsonResponse(data)

