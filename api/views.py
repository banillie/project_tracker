import json
from django.forms.models import model_to_dict
# from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from projects.models import Project
from projects.serializers import ProjectSerializer

from engagements.models import Engagement
from engagements.serializers import EngagementSerializer

# def api_home(request, *args, **kwargs):
    # # request -> HttpRequest -> Django
    # # request.body
    # body = request.body # byte string of json
    # data = {}
    # try:
    #     data = json.loads(body)  # string of Json data -> Python Dict
    # except:
    #     pass
    # # print(data)
    # print(request.GET)
    # print(request.POST)
    # data["params"] = dict(request.GET)
    # data['headers'] = dict(request.headers)
    # # print(request.headers)
    # data["content_type"] = request.content_type
    #
    # return JsonResponse(data)


# Serialization: modal instance (modal_data) -> turn into a Python Dict -> return JSON to client.

# Project.objects.all().order_by("?").first()  # ? means random selection


# @api_view(["GET", "POST"])
# def api_home(request, *args, **kwargs):
#     """
#     DRF API VIEW
#     """
#     instance = Project.objects.all().order_by("?").first()
#     data = {}
#     if instance:
#         # data = model_to_dict(instance, fields=['id', 'name', 'type', 'scope'])
#         data = ProjectSerializer(instance).data
#
#     # instance = Engagement.objects.all().order_by("?").first()
#     # data = {}
#     # if instance:
#     #     # data = model_to_dict(instance)
#     #     data = EngagementSerializer(instance).data
#     #
#     return Response(data)

@api_view(["POST", "GET"])
def api_home(request, *args, **kwargs):
    serializer = ProjectSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        # instance = serializer.save()
        # instance = serializer.save()
        # instance = form.
        print(serializer.data)
        return Response(serializer.data)

    # serializer = EngagementSerializer(data=request.data)
    # if serializer.is_valid(raise_exception=True):
    #     # instance = serializer.save()
    #     # instance = serializer.save()
    #     # instance = form.
    #     print(serializer.data)
    #     return Response(serializer.data)


