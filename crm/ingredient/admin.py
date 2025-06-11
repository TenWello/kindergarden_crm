from django.contrib import admin
from .models import Ingredient

@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ['name', 'quantity', 'expiration_date']
    search_fields = ['name']
