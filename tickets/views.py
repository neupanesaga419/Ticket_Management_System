from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from tickets.models import Tickets

from tickets.serializers import TicketsSerializer


class ViewTickets(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request):
        data = Tickets.objects.filter(user=request.user.id)
        serializer = TicketsSerializer(data, many=True)
        return Response(serializer.data)

    def post(self,request):
        data = request.data
        user = request.user.id
        data['user'] = user
        serializer = TicketsSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"msg":"Tickets Successfully Created","ticket data":serializer.data})