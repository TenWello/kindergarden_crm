from django.contrib import admin
from .models import Payment

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ("id", "total_money", "total_salary", "total_product_price", "total_benefit", "created_at")
    search_fields = ("total_money",)
    filter_horizontal = ("users", "inventories")
