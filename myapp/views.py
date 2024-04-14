# myapp/views.py

from django.shortcuts import render
from .models import Card

def card_list(request):
    cards = Card.objects.all()
    return render(request, 'menu.html', {'cards': cards})

# views.py

from django.shortcuts import render, redirect
from .forms import TableOrderForm

def order_form(request):
    if request.method == 'POST':
        form = TableOrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_url')  # Redirect to a success page
    else:
        form = TableOrderForm()
    return render(request, 'menu.html', {'form': form})
