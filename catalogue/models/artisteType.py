from django.db import models
from .artist import Artist
from .type import Type

class ArtisteType(models.Model):
    artiste_type_id = models.AutoField(primary_key=True)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)

    class Meta:
        db_table = "artiste_type"

    def __str__(self):
        return f'{self.artist} - {self.type}'
