# myapp/views.py

from django.shortcuts import render
from .models import Card

def card_list(request):
    cards = Card.objects.all()
    return render(request, 'menu.html', {'cards': cards})


from django.shortcuts import render
from .forms import OrderForm
from decimal import Decimal
from django.utils import timezone

def order_view(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            total_price = request.POST.get('total_price')
            if total_price:
                try:
                    order.total_price = Decimal(total_price)
                except ValueError:
                    pass  # Handle invalid Decimal values here
            order.order_details = request.POST.get('order_details')
            
            # Save the current time as the timestamp
            order.timestamp = timezone.now()
            
            order.save()
            return render(request, 'menu.html', {'form': form, 'order_placed': True})  # Render the same page with an indication that the order was successfully placed
    else:
        form = OrderForm()
    return render(request, 'menu.html', {'form': form})
