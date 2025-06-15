from django.db import models
from category.models import Category

class Product(models.Model):
    UNIT_KG = 'kg'
    UNIT_L = 'litr'
    UNIT_PCS = 'dona'
    UNIT_CHOICES = [
        (UNIT_KG, 'Kilogram'),
        (UNIT_L, 'Litr'),
        (UNIT_PCS, 'Dona'),
    ]

    name = models.CharField(max_length=100)
    category_id = models.ForeignKey(Category, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField(null=True, blank=True)
    unit = models.CharField(max_length=10, choices=UNIT_CHOICES, default=UNIT_KG, verbose_name="O‘lchov birligi")
    total_cost = models.PositiveIntegerField(null=True, blank=True)
    delivered_date = models.DateField(null=True, blank=True)
    best_before = models.DateField(null=True, blank=True)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def unit_price(self):
        if self.quantity and self.quantity > 0:
            return self.total_cost / self.quantity
        return 0

    def __str__(self):
        return self.name
