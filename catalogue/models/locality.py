# catalogue/models/locality.py
from django.db import models

class Locality(models.Model):
    locality_id = models.AutoField(primary_key=True)
    postal_code = models.CharField(max_length=6)
    locality = models.CharField(max_length=60)

    class Meta:
        db_table = "localities"
