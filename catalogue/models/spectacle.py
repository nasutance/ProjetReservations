# catalogue/models/spectacle.py
from django.db import models
from .location import Location

class Spectacle(models.Model):
    spectacle_id = models.BigAutoField(primary_key=True)
    slug = models.CharField(max_length=60, unique=True)
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=255, null=True)
    poster_url = models.CharField(max_length=255, null=True)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, related_name='spectacles')
    duration = models.SmallIntegerField(null=True)
    created_in = models.CharField(max_length=4, null=True)
    bookable = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)

    class Meta:
        db_table = "spectacles"
