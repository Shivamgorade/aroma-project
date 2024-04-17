# models.py

from datetime import timezone
from django.db import models


class Card(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='card_images/')

    def __str__(self):
        return self.name


from django.db import models
from django.utils import timezone

class Order(models.Model):
    name = models.CharField(max_length=100)
    table_number = models.IntegerField()
    order_details = models.TextField()
    note = models.TextField(blank=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    timestamp = models.DateTimeField()
    
    def __str__(self):
        current_time = timezone.localtime(self.timestamp).strftime('%I:%M %p')  # Get current time in the timezone of the order
        return f"Order #{self.id} - {self.name} - Time {current_time}"
