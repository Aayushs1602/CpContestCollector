from rest_framework import serializers
from .models import Contest

class ContestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contest
        fields = ['id', 'platform', 'contest_id', 'title', 'start_time', 'duration', 'url']
