# inventory/admin.py
from django.contrib import admin
from .models import Inventory

@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'product', 'quantity', 'total', 'created_at']
    readonly_fields = ('quantity', 'total')

