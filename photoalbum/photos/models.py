from django.db import models

class Photo(models.Model):
    latitude = models.DecimalField(decimal_places=6, max_digits=9)
    longitude = models.DecimalField(decimal_places=6, max_digits=9)
    uploader = models.CharField(max_length=30)
    image = models.ImageField(upload_to="images")
