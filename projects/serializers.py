from rest_framework import serializers
from rest_framework.reverse import reverse

from .models import Project


class ProjectSerializer(serializers.ModelSerializer):
    my_slug = serializers.SerializerMethodField(read_only=True)
    # url = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(
        view_name='project-detail',
        lookup_field='slug',
    )
    # cost = serializers.IntegerField(write_only=True)

    class Meta:
        model = Project
        fields = [
            'url',
            'pk',
            'id',
            'name',
            'type',
            'tier',
            'abbreviation',
            'dft_group',
            # 'cost',
            'scope',
            'my_slug',
            'slug',
        ]

    # # could do in perform_create in views also.
    # def create(self, validated_data):
    #     # returns back the default value or inherited class model serializer.
    #     cost = validated_data.pop('cost')
    #     obj = super().create(validated_data)
    #     print(cost, obj)
    #     return obj

    # def update(self, instance, validated_data):
    #     pass

    # def get_url(self, obj):
    #     request = self.context.get('request')  # self.request
    #     if request is None:
    #         return None
    #     # rest_framework reverse is different to django reverse
    #     return reverse("project-detail", kwargs={"pk": obj.pk}, request=request)

    def get_my_slug(self, obj):
        if not hasattr(obj, 'id'):
            return None
        if not isinstance(obj, Project):
            return None
        return obj.sluggy_slug()
