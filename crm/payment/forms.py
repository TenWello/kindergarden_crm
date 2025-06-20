from django import forms
from .models import Payment

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = [
            'total_money', 'total_salary', 'total_product_price',
            'users', 'inventories', 'total_benefit'
        ]
