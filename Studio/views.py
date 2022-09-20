from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser,IsAuthenticated

from Studio.serializers import StudioSerializer
from Studio.models import Studio


class StudioAPIView(viewsets.ModelViewSet):

    serializer_class = StudioSerializer
    queryset = Studio.objects.filter(still_playing=True)

    def get_permissions(self):

        list_activities = ["create","partial_update", "destroy", "update"]
        
        if self.action in list_activities:
            permission_classes = [IsAdminUser]
        
        else:
            permission_classes = [IsAuthenticated]

        return [permission() for permission in permission_classes]
    