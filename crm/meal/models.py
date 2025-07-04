from django.db import models
from product.models import Product



class Meal(models.Model):
    food_name = models.CharField(max_length=100)
    products = models.ManyToManyField(Product, related_name='meals', blank=True)  # eski mahsulot
    ingredients = models.ManyToManyField('ingredient.Ingredient', related_name='meals', blank=True, verbose_name="Ingredientlar")
    portion = models.PositiveIntegerField(default=1, verbose_name="Porsiya soni")
    available_portions = models.IntegerField(default=0, help_text="Mavjud porsiyalar soni")
    cooking_time = models.DurationField(null=True, blank=True)
    recipe = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.available_portions = self.portion
        super().save(*args, **kwargs)

