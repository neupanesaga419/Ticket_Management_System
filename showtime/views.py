from datetime import date
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins
from rest_framework import viewsets,generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from showtime.models import ShowTime, Shows
from showtime.serializers import ShowTimeSerializer, ShowsSerializer
from showtime.filters import MyDateFilter



class ShowListAPIView(generics.ListAPIView):
    serializer_class = ShowTimeSerializer
    queryset = ShowTime.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = MyDateFilter

    


class ShowTimeAPIView(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    viewsets.GenericViewSet):

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
