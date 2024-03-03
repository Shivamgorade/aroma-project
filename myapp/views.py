# views.py
from django.shortcuts import render, redirect
from .models import Category, MenuItem, Order
from .forms import OrderForm

def menu(request):
    categories = Category.objects.all()
    menu_items = MenuItem.objects.all()
    form = OrderForm()
    return render(request, 'menu.html', {'categories': categories, 'menu_items': menu_items, 'form': form})

def place_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('menu')
    return redirect('menu')
