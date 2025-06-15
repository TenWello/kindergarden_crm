from django.db import models
from meal.models import Meal
from user.models import User

class Service(models.Model):
    meal = models.ForeignKey(Meal, on_delete=models.SET_NULL, null=True)
    served_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        limit_choices_to={'role__in': [User.ROLE_CHEF, User.ROLE_ADMIN]}
    )
    portion_count = models.IntegerField(default=0)
    served_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.meal} - {self.served_by}"
