from rest_framework import serializers

from .models import Project


class ProjectSerializer(serializers.ModelSerializer):
    my_slug = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Project
        fields = [
            'pk',
            'id',
            'name',
            'type',
            'tier',
            'abbreviation',
            'scope',
            'my_slug',
            'slug',
        ]

    def get_my_slug(self, obj):
        if not hasattr(obj, 'id'):
            return None
        if not isinstance(obj, Project):
            return None
        return obj.sluggy_slug()
