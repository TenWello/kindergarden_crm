from django.contrib import admin
from .models import Meal

@admin.register(Meal)
class MealAdmin(admin.ModelAdmin):
    list_display = ('food_name', 'portion', 'cooking_time', 'created_at', 'updated_at')
    search_fields = ('food_name', 'description', 'recipe')
    filter_horizontal = ('products',)
