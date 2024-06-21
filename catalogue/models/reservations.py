from django.db import models
from .users import Users

class Reservations(models.Model):
    reservation_id = models.AutoField(primary_key=True)
    booking_date = models.DateTimeField()
    status = models.CharField(max_length=255)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)

    class Meta:
        db_table = "reservations"

    def __str__(self):
        return f'{self.user} - {self.booking_date} - {self.status}'
