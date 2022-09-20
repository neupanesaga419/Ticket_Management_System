from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


def age_validator(data):

    if 16 > data or data > 70:
        raise ValidationError("User Age Must Be Greater Than 16 and Smaller Than 70")
    
GENDER = (("MALE","MALE"), ("FEMALE", "FEMALE"), ("OTHERS", "OTHERS"))

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    profile_image = models.ImageField(upload_to="user_image",)
    full_name = models.CharField(max_length=255)
    age = models.IntegerField(validators=[age_validator])
    address = models.CharField(max_length=350)
    gender = models.CharField(choices=GENDER, max_length=20)

    def __str__(self):
        return str(self.full_name)

