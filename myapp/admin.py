from django.contrib import admin
from .models import Card
from .models import TableOrders


admin.site.register(Card)
class TableOrderAdmin(admin.ModelAdmin):
    list_display = ('name', 'table_number', 'note', 'timestamp')

    def timestamp_formatted(self, obj):
        return obj.timestamp.strftime('%d-%m-%Y %I:%M:%S %p')

admin.site.register(TableOrders, TableOrderAdmin)

