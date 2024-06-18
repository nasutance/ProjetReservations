# catalogue/models/type.py
from django.db import models

class Type(models.Model):
    type_id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=60)

    class Meta:
        db_table = "types"
