from django.db import models

# Define the Product model
class Product(models.Model):
    # Product name (maximum length of 255 characters)
    name = models.CharField(max_length=255)
    # Optional product description
    description = models.TextField(blank=True)
    # Product price as a floating-point number
    price = models.FloatField()
    # Stock quantity as a positive integer
    stock = models.PositiveIntegerField()

    # String representation of the Product object
    def __str__(self):
        return self.name
