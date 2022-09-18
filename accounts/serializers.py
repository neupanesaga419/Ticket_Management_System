from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.models import User



class CustomTokenObtainSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user:User):
        token =  super().get_token(user)
        token["username"] = user.username
        token["email"] = user.email
        
        return token
    


class UserCreationSerializer(serializers.ModelSerializer):

    password2 = serializers.CharField(style={"input-type":"password"}, write_only=True)
    email = serializers.EmailField(max_length=255)
    class Meta:
        model = User
        fields = ["username", "email", "password", "password2"]

        extra_kwargs = {
            "password":{"write_only":True,}
        }
    
    def validate_email(self,value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("User has been already created via this email.\
please try new one")
        return value

    def validate(self, attrs):
        
        valid_data = super().validate(attrs)
        password = valid_data['password']
        password2 = valid_data['password2']

        if password != password2:
            raise serializers.ValidationError({"password_validator":"Two Passwords Didnot Match."})
    
        return valid_data

    def save(self):
        password = self.validated_data["password"]
        email = self.validated_data["email"]
        username = self.validated_data['username']
        account = User(username=username, email=email)
        account.set_password(password)
        account.save()
        return account
        
