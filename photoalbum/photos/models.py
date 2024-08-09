from django.db import models

class Photo(models.Model):
    latitude = models.DecimalField()
    longitude = models.DecimalField()
