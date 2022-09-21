from rest_framework import viewsets, generics
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from userprofiles.serializers import UserProfileSerializer
from userprofiles.models import UserProfile
from userprofiles.permissions import IsProfileBelongsTo


class ViewProfile(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request):
        if not request.user.is_superuser:
            data = UserProfile.objects.filter(user=request.user.id)
        else:
            data = UserProfile.objects.all()
        print(data)
        serializer = UserProfileSerializer(data, many=True)
        return Response(serializer.data)

    def post(self,request):
        data = request.data
        user = request.user.id
        data['user'] = user
        serializer = UserProfileSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"msg":"UserProfile  Successfully Created","profile data":serializer.data})


class UserProfileDetails(generics.RetrieveUpdateDestroyAPIView):

    serializer_class =  UserProfileSerializer
    queryset = UserProfile.objects.all()
    permission_classes = [IsProfileBelongsTo]
