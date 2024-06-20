# catalogue/models/representation.py
from django.db import models
from .location import Location
from .spectacle import Spectacle

class Representation(models.Model):
    representation_id = models.BigAutoField(primary_key=True, verbose_name='representation_id')
    spectacle = models.ForeignKey(Spectacle, on_delete=models.CASCADE, related_name='representations')
    schedule = models.DateTimeField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='representations')

    class Meta:
        db_table = "representations"
