# catalogue/models/role.py
from django.db import models

class Role(models.Model):
    role_id = models.AutoField(primary_key=True)
    role = models.CharField(max_length=30)

    class Meta:
        db_table = "roles"
