# ingredient/forms.py
from django import forms
from .models import Ingredient

class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ['name', 'quantity', 'expiration_date']
        widgets = {
            'expiration_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }
