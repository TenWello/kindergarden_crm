from django.contrib import admin
from .models import Meal


@admin.register(Meal)
class MealAdmin(admin.ModelAdmin):
    list_display = ('food_name', 'get_products', 'portion', 'cooking_time', 'created_at')
    list_filter = ('created_at', 'cooking_time')
    search_fields = ('food_name', 'recipe', 'ingredient', 'description')
    readonly_fields = ('created_at', 'updated_at')

    def get_products(self, obj):
        return ", ".join([str(p) for p in obj.products.all()])
    get_products.short_description = 'Products'

