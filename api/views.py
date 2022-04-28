import json
from django.http import JsonResponse


def api_home(request, *args, **kwargs):
    # request -> HttpRequest -> Django
    # request.body
    body = request.body # byte string of json
    data = {}
    try:
        data = json.loads(body)  # string of Json data -> Python Dict
    except:
        pass
    # print(data)
    print(request.GET)
    print(request.POST)
    data["params"] = dict(request.GET)
    data['headers'] = dict(request.headers)
    # print(request.headers)
    data["content_type"] = request.content_type

    return JsonResponse(data)
