from django import forms
from .models import Meal

class MealForm(forms.ModelForm):
    class Meta:
        model = Meal
        fields = ['food_name', 'products', 'portion', 'cooking_time', 'recipe', 'description']
        widgets = {
            'products': forms.CheckboxSelectMultiple,
        }
