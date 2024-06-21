from django.db import models
from .artisteType import ArtisteType
from .spectacle import Spectacle

class ArtisteTypeSpectacle(models.Model):
    artiste_type_spectacle_id = models.AutoField(primary_key=True)
    artiste_type = models.ForeignKey(ArtisteType, on_delete=models.CASCADE)
    spectacle = models.ForeignKey(Spectacle, on_delete=models.CASCADE)

    class Meta:
        db_table = "artiste_type_spectacle"

    def __str__(self):
        return f'{self.artiste_type} - {self.spectacle}'
