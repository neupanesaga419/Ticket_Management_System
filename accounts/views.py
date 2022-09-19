from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.decorators import api_view
from rest_framework.response import Response

import qrcode as qr

from accounts.serializers import CustomTokenObtainSerializer, UserCreationSerializer


class CustomTokenObtainPairView(TokenObtainPairView):

    serializer_class =  CustomTokenObtainSerializer

    def post(self, request, *args, **kwargs):
        post_data =  super().post(request, *args, **kwargs)
        get_data = self.serializer_class(data=request.data)
        get_data.is_valid(raise_exception=True)
        access_token = get_data.validated_data['access']
        img = qr.make(access_token)
        qrname = f"{request.data['username']}.png"
        # print(request.data['username'])
        # print(qrname)
        img.save(qrname)
        return post_data


@api_view(['POST'])
def register_user(request):

    if request.method == "POST":
        serializer = UserCreationSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        account = serializer.save()
        return Response({"msg":f'{account.username} has been successfully created',"data":serializer.data})