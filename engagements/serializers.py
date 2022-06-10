from rest_framework import serializers

from .models import Engagement, EngagementTopic


class EngagementSerializer(serializers.ModelSerializer):

    class Meta:
        model = Engagement
        fields = '__all__'


class EngagementTopicSerializer(serializers.ModelSerializer):

    class Meta:
        model = EngagementTopic
        fields = '__all__'
