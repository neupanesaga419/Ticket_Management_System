
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from showtime.models import ShowTime, Shows
from showtime.serializers import ShowTimeSerializer, ShowsSerializer


class ShowTimeAPIView(viewsets.ModelViewSet):

    serializer_class = ShowTimeSerializer
    queryset = ShowTime.objects.filter()

    def get_permissions(self):

        list_activities = ["create","partial_update", "destroy", "update"]
        
        if self.action in list_activities:
            permission_classes = [IsAdminUser]
        
        else:
            permission_classes = [IsAuthenticated]

        return [permission() for permission in permission_classes] 



class ShowsAPIView(viewsets.ModelViewSet):
    serializer_class = ShowsSerializer
    queryset = Shows.objects.filter()

    def get_permissions(self):

        list_activities = ["create","partial_update", "destroy", "update"]
        
        if self.action in list_activities:
            permission_classes = [IsAdminUser]
        
        else:
            permission_classes = [IsAuthenticated]

        return [permission() for permission in permission_classes] 
