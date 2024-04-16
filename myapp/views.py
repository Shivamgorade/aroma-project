# myapp/views.py

from django.shortcuts import render
from .models import Card

def card_list(request):
    cards = Card.objects.all()
    return render(request, 'menu.html', {'cards': cards})


from django.shortcuts import render, redirect
from .forms import OrderForm
from decimal import Decimal

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
            order.save()
            return redirect('success_page')  # Redirect to a success page
    else:
        form = OrderForm()
    return render(request, 'menu.html', {'form': form})
