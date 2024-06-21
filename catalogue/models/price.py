from django.db import models

class Price(models.Model):
    price_id = models.AutoField(primary_key=True)
    end_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateField()
    type = models.CharField(max_length=255)

    class Meta:
        db_table = "prices"

    def __str__(self):
        return f'{self.type} - {self.price}'
