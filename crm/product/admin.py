from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'category_id', 'quantity','unit', 'total_cost', 'unit_price',
        'delivered_date', 'best_before', 'created_at', 'updated_at'
    )
    list_filter = ('category_id', 'delivered_date', 'best_before')
    search_fields = ('name',)
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)

    def unit_price(self, obj):
        return f"{obj.unit_price:,.2f}"
    unit_price.short_description = 'Bir dona narx'
