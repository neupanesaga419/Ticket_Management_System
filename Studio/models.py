from django.db import models
from django.core.validators import MinValueValidator


STUDIO_TYPES = (("MULTIPLEX","MULTIPLEX"),("3D","3D"),("2D","2D"))

class Studio(models.Model):
    name = models.CharField(max_length=255)
    studio_details = models.TextField()
    studio_type = models.CharField(choices=STUDIO_TYPES,max_length=100)
    still_playing = models.BooleanField(default=True)
    capacity = models.IntegerField(validators=[MinValueValidator(0)])

    def __str__(self):
        return self.name