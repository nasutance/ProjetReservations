from django.db import models

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=255)
    firstname = models.CharField(max_length=255)
    langue = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    login = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    class Meta:
        db_table = "users"

    def __str__(self):
        return f'{self.firstname} {self.lastname}'
