from os import name
from django.contrib import admin
from .models import Card
from .models import Order


admin.site.register(Card)

from django.contrib import admin
from .models import Order
from django.utils import timezone

class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_info', 'customer_name', 'current_time')  # Define the list display fields

    def order_info(self, obj):
        return f"Order #{obj.id}"  # Display order info

    def customer_name(self, obj):
        return obj.name  # Display customer name

    def current_time(self, obj):
        return timezone.localtime(obj.timestamp).strftime('%I:%M %p')  # Format and display current time

    order_info.short_description = 'Order Info'  # Set the column header for order info
    customer_name.short_description = 'Customer Name'  # Set the column header for customer name
    current_time.short_description = 'Order Time'  # Set the column header for current time

admin.site.register(Order, OrderAdmin)