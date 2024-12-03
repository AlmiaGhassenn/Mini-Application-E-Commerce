from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.FloatField()
    stock = models.PositiveIntegerField()

    def __str__(self):
        return self.name