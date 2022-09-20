from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from movie.models import Movie
from movie.serializers import MovieSerializer


class MovieAPIView(viewsets.ModelViewSet):

    serializer_class = MovieSerializer
    queryset = Movie.objects.filter(is_availiable=True)

    def get_permissions(self):

        list_activities = ["create","partial_update", "destroy", "update"]
        
        if self.action in list_activities:
            permission_classes = [IsAdminUser]
        
        else:
            permission_classes = [IsAuthenticated]

        return [permission() for permission in permission_classes] 