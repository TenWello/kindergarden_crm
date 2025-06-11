from django import forms
from .models import Inventory

class InventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = ['name', 'product', 'ingredient', 'quantity', 'delivery_at', 'note']

    def clean(self):
        cleaned_data = super().clean()
        product = cleaned_data.get("product")
        ingredient = cleaned_data.get("ingredient")
        if not product and not ingredient:
            raise forms.ValidationError("Kamida bitta (Mahsulot yoki Ingredient) tanlansin!")
        if product and ingredient:
            raise forms.ValidationError("Faqat bittasi tanlansin: Mahsulot yoki Ingredient!")
        return cleaned_data
