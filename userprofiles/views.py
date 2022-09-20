from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response

from userprofiles.serializers import UserProfileSerializer
from userprofiles.models import UserProfile
from userprofiles.permissions import IsProfileBelongsTo



class UserProfileViewSet(viewsets.ModelViewSet):

    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated, IsProfileBelongsTo]
    # queryset = UserProfile.objects.all()

    def get_queryset(self):

        if self.request.user.is_superuser:
            return UserProfile.objects.all()
        
        return UserProfile.objects.filter(user=self.request.user.id)


    def create(self, request):
        data = request.data
        user = request.user.id
        data['user'] = user
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"msg":"UserProfile Successfully Created","Profile data":serializer.data})
    
    
    def update(self, request, pk=None):
        data = request.data
        user = request.user.id
        data['user'] = user
        obj = UserProfile.objects.get(id=pk)
        serializer = self.serializer_class(obj,data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"msg":"UserProfile Updated Successfully","Profile data":serializer.data})
    
    def partial_update(self, request, pk=None):
        data = request.data
        user = request.user.id
        data['user'] = user
        obj = UserProfile.objects.get(id=pk)
        serializer = self.serializer_class(obj,data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"msg":"UserProfile Updated Successfully","Profile data":serializer.data})
    