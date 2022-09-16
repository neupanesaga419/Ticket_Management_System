from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser,IsAuthenticated

from Studio.serializers import StudioSerializer
from Studio.models import Studio


class StudioGetAV(viewsets.GenericViewSet):

    serializer_class = StudioSerializer
    queryset = Studio.objects.all()
    permission_classes = [IsAuthenticated]

    def list(self, request):
        query_list = self.get_queryset()
        serializer = self.serializer_class(query_list, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk):
        query_list = self.get_queryset()
        query_obj = get_object_or_404(query_list, pk=pk)
        serializer = self.serializer_class(query_obj)
        return Response(serializer.data)


class StudioCreateAV(generics.CreateAPIView):

    serializer_class = StudioSerializer
    queryset = Studio.objects.all()
    permission_classes = [IsAdminUser]


    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class StudioUpdateDeleteAV(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = StudioSerializer
    queryset = Studio.objects.all()
    permission_classes = [IsAdminUser]

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)