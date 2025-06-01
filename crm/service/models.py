from django.db import models
from meal.models import Meal
from user.models import User

class Service(models.Model):
    meal_id = models.ForeignKey('Meal', on_delete=models.SET_NULL)
    served_by = models.ForeignKey('User', on_delete=models.SET_NULL)
    portion_count = models.IntegerField(default=0)
    served_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.served_by.name