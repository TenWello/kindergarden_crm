# ingredient/models.py
from django.db import models
from meal.models import Meal
from product.models import Product

class Ingredient(models.Model):
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE, related_name='ingredients')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='ingredients')
    quantity_per_portion = models.FloatField("Bir porsiyadagi miqdor")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.meal.food_name} uchun {self.product.name} ({self.quantity_per_portion})"
