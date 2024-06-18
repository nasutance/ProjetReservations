from django.db import models

class ArtType(models.Model):
    type_name = models.CharField(max_length=50)
