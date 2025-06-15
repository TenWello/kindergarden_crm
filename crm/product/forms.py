# product/forms.py
from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'name', 'category_id', 'quantity', 'unit', 'total_cost',
            'delivered_date', 'best_before'
        ]
        widgets = {
            'quantity': forms.NumberInput(attrs={
                'class': 'form-control',
                'style': 'width: 80px; display:inline-block;'
            }),
            'unit': forms.Select(attrs={
                'class': 'form-select',
                'style': 'width: 120px; display:inline-block; margin-left:8px;'
            })
        }