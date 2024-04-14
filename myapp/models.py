# models.py

from django.db import models
from datetime import datetime

class Card(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='card_images/')
   

    def __str__(self):
        return self.name

class TableOrders(models.Model):
    name = models.CharField(max_length=100)
    table_number = models.IntegerField()
    note = models.TextField()
    timestamp = models.DateTimeField()
   

    def __str__(self):
       return f"{self.name} - Table {self.table_number} - Time {self.timestamp.strftime('%d-%m-%Y %I:%M:%S %p')}"

    def save(self, *args, **kwargs):
        if not self.id:  # Check if it's a new object
            self.timestamp = datetime.now()  # Set current device time as timestamp
        super(TableOrders, self).save(*args, **kwargs)






