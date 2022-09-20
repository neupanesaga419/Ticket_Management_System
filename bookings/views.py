from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from accounts.permissions import IsOnlyTicketUser

from bookings.models import Bookings
from bookings.serializers import BookingsSerializer

class ViewBookings(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request):
        if not request.user.is_superuser:
            data = Bookings.objects.filter(user=request.user.id)
        else:
            data = Bookings.objects.all()
        serializer = BookingsSerializer(data, many=True)
        return Response(serializer.data)

    def post(self,request):
        data = request.data
        user = request.user.id
        data['user'] = user
        serializer = BookingsSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"msg":"Booking Successfully Created","Bookings data":serializer.data})


class BookingsDetails(generics.RetrieveUpdateDestroyAPIView):

    serializer_class =  BookingsSerializer
    queryset = Bookings.objects.all()
    permission_classes = [IsOnlyTicketUser]
