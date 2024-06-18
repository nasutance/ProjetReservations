from django.db import models

class Artist(models.Model):
    artist_id = models.BigAutoField(primary_key=True, verbose_name='artist_id')
    firstname = models.CharField(max_length=60)
    lastname = models.CharField(max_length=60)

    class Meta:
        db_table = "artists"
