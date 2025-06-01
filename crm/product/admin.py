from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category_id', 'quantity',
                    'total_cost', 'delivered_date', 'best_before', 'created_at', 'updated_at',)
    list_filter = ('category_id', 'delivered_date', 'best_before')
    search_fields = ('name',)
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)
