# service/forms.py
from django import forms
from django.core.exceptions import ValidationError
from .models import Service
from meal.models import Meal

class ServiceForm(forms.ModelForm):
    class Meta:
        model  = Service
        fields = ['meal', 'served_by', 'portion_count']

    def clean(self):
        cleaned = super().clean()
        meal   = cleaned.get('meal')
        count  = cleaned.get('portion_count')

        if meal and count:
            if meal.available_portions < count:
                raise ValidationError(
                    f"Yetarli porsiya yo‘q. Mavjud: {meal.available_portions}, so‘raldi: {count}"
                )
        return cleaned

    def save(self, commit=True):
        # 1) Service yozuvini saqlash uchun avval instance hosil qilamiz, lekin DBga hali yozmaymiz
        instance = super().save(commit=False)

        # 2) Meal modelidagi porsiya sonini ayiramiz
        meal = instance.meal
        meal.available_portions -= instance.portion_count
        meal.save()

        # 3) Service instance’ni DBga yozamiz
        if commit:
            instance.save()
        return instance
