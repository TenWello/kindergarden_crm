from django.contrib import admin
from .models import Inventory

@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'product', 'total', 'created_at')
    readonly_fields = ('delivery_at', 'total')

