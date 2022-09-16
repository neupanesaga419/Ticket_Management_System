from rest_framework import serializers
from showtime.models import ShowTime


class ShowTimeSerializer(serializers.ModelSerializer):

    class Meta:
        model = ShowTime
        fields = "__all__"
