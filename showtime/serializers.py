from rest_framework import serializers
from showtime.models import ShowTime, Shows


class ShowTimeSerializer(serializers.ModelSerializer):

    class Meta:
        model = ShowTime
        fields = "__all__"


class ShowsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Shows
        fields = "__all__"