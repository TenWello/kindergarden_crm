from django.db import models
from product.models import Product


class Meal(models.Model):
    products = models.ManyToManyField(Product)
    food_name = models.CharField(max_length=100)
    portion = models.DateTimeField(auto_now_add=True)
    cooking_time = models.DurationField(null=True, blank=True)
    recipe = models.TextField(null=True, blank=True)
    ingredient = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.food_name
