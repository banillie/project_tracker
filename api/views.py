from django.http import JsonResponse
from django.forms.models import model_to_dict

from rest_framework.decorators import api_view
from rest_framework.response import Response

from projects.models import Project
from projects.serializers import ProjectSerializer


@api_view(["GET"])
def api_home(request, *args, **kwargs):
    instance = Project.objects.all().order_by("?").first()
    # instance = Project.objects.all()
    data = {}
    data = ProjectSerializer(instance).data
    return Response(data)

