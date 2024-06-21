from django.db import models
from .prices import Prices
from .representation import Representation
from .reservations import Reservations

class RepresentationReservation(models.Model):
    representation_reservation_id = models.AutoField(primary_key=True)
    price = models.ForeignKey(Prices, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()
    representation = models.ForeignKey(Representation, on_delete=models.CASCADE)
    reservation = models.ForeignKey(Reservations, on_delete=models.CASCADE)

    class Meta:
        db_table = "representation_reservation"

    def __str__(self):
        return f'{self.reservation} - {self.representation} - {self.quantity} - {self.price}'
