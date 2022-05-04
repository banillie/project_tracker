from rest_framework import mixins, viewsets

from .models import Project
from .serializers import ProjectSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    """
    GET -> list -> QuerySet
    GET -> retrieve -> Product Instance Detail View
    POST -> create -> New Instance
    PUT -> update
    PATCH -> partial update
    DELETE -> destroy
    Doesn't provide granularity over urls.
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    lookup_field = 'pk'  # default


class ProjectGenericViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet
):
    """
    GET -> list -> QuerySet
    GET -> retrieve -> Product Instance Detail View
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    lookup_field = 'pk'  # default
