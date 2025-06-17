# ingredient/models.py
from django.db import models
from meal.models import Meal
from product.models import Product
import datetime

class Ingredient(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nomi")
    quantity = models.PositiveIntegerField(verbose_name="Miqdor (gramm)")

    expiration_date = models.DateField(verbose_name="Saqlash muddati", default=datetime.date.today)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name



