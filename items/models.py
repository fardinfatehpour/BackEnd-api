from django.db import models

class Item(models.Model):
    item_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
