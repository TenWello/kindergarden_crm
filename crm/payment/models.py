from django.db import models

from crm.inventory.models import Inventory
from crm.user.models import User


class Payment(models.Model):
    total_money = models.BigIntegerField(null=True, blank=True, default=0)
    total_salary = models.BigIntegerField(null=True, blank=True, default=0)
    total_product_price = models.BigIntegerField(null=True, blank=True, default=0)
    user_id = models.ManyToManyField(User, related_name='payments_user')
    inventory_id = models.ManyToManyField(Inventory, related_name='payments_inventory')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    generated_at = models.DateTimeField(auto_now_add=True)
    total_benefit = models.BigIntegerField(null=True, blank=True, default=0)

    def __str__(self):
        return self.total_money

