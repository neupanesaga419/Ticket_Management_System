
from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from showtime.models import ShowTime, Shows
from showtime.serializers import ShowTimeSerializer, ShowsSerializer


class ShowTimeListAV(generics.ListCreateAPIView):

    permission_classes = [IsAdminUser]
    serializer_class = ShowTimeSerializer
    queryset = ShowTime.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ShowTimeDetailAV(generics.RetrieveUpdateDestroyAPIView):

    permission_classes = [IsAdminUser]
    serializer_class = ShowTimeSerializer
    queryset = ShowTime.objects.all()

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class ShowsListAV(generics.ListAPIView):

    serializer_class = ShowsSerializer
    queryset = Shows.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class ShowsCreateAV(generics.CreateAPIView):

    permission_classes = [IsAdminUser]
    serializer_class = ShowsSerializer
    queryset = Shows.objects.all()

      
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ShowsDetailsAV(generics.RetrieveUpdateDestroyAPIView):

    permission_classes = [IsAdminUser]
    serializer_class = ShowsSerializer
    queryset = Shows.objects.all()

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

