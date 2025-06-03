# product/forms.py
from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'name', 'category_id', 'quantity', 'total_cost',
            'delivered_date', 'best_before'
        ]
