from rest_framework import serializers

from .models import Engagement


class EngagementSerializer(serializers.ModelSerializer):

    class Meta:
        model = Engagement
        fields = [
            'date',
            'projects',
            'stakeholders'
        ]
