from django import forms
from .models import TableOrders

class TableOrderForm(forms.ModelForm):
    class Meta:
        model = TableOrders
        fields = ['name', 'table_number', 'note']
