from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from accounts.serializers import CustomTokenObtainSerializer, UserCreationSerializer


class CustomTokenObtainPairView(TokenObtainPairView):

    serializer_class =  CustomTokenObtainSerializer


@api_view(['POST'])
def register_user(request):

    if request.method == "POST":
        serializer = UserCreationSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        account = serializer.save()
        return Response({"msg":f'{account.username} has been successfully created',"data":serializer.data})