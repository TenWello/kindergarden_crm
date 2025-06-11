# inventory/models.py
from django.db import models
from product.models import Product
from ingredient.models import Ingredient
from django.utils import timezone


class Inventory(models.Model):
    name = models.CharField(max_length=100, verbose_name="Inventar nomi")
    product = models.ForeignKey(Product, null=True, blank=True, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, null=True, blank=True, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=True, blank=True, verbose_name="Miqdori (gramm)")
    delivery_at = models.DateField(verbose_name="Keltirilgan sana", default=timezone.now)  # bo'lishi kerak
    note = models.CharField(max_length=255, null=True, blank=True, verbose_name="Izoh")    # bo'lishi kerak
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    total = models.BigIntegerField(null=True, blank=True)
    def __str__(self):
        return self.name

