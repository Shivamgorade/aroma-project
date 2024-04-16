# models.py

from django.db import models
from datetime import datetime

class Card(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='card_images/')

    def __str__(self):
        return self.name



from django.db import models


class Order(models.Model):
    name = models.CharField(max_length=100)
    table_number = models.IntegerField()
    order_details = models.TextField()
    note = models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, null=True)  # Making total_price nullable



    def __str__(self):
        return f"Order #{self.id} - {self.name}"