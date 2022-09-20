from rest_framework import serializers

from bookings.models import Bookings


class BookingsSerializer(serializers.ModelSerializer):

    class Meta:
        fields = "__all__"
        model = Bookings