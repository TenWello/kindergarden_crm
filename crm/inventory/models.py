# inventory/models.py
from django.db import models
from product.models import Product

class Inventory(models.Model):
    name = models.CharField(max_length=100)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    delivery_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    quantity = models.IntegerField(null=True, blank=True)
    total = models.BigIntegerField(null=True, blank=True)

    def save(self, *args, **kwargs):
        # Agar product tanlangan bo‘lsa va quantity yoki total kiritilmagan bo‘lsa
        if self.product:
            if not self.quantity:
                self.quantity = self.product.quantity
            if not self.total:
                self.total = self.product.total_cost
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
