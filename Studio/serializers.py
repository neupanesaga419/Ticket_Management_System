from rest_framework import serializers
from Studio.models import Studio


class StudioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Studio
        fields = "__all__"
