from django.db import models
from inventory.models import Inventory
from user.models import User


class Payment(models.Model):
    total_money = models.BigIntegerField(null=True, blank=True, default=0, verbose_name='Kassadagi jami pul')
    total_salary = models.BigIntegerField(null=True, blank=True, default=0, verbose_name='Jami oyliklar')
    total_product_price = models.BigIntegerField(null=True, blank=True, default=0,
                                                 verbose_name='Sotib olingan mahsulotlarga ketgan pul')
    users = models.ManyToManyField(User, related_name='payments_user', verbose_name='Ishchilar')
    inventories = models.ManyToManyField(Inventory, related_name='payments_inventory', verbose_name='Inventarlar')
    total_benefit = models.BigIntegerField(null=True, blank=True, default=0, verbose_name='Jami foyda')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Kassa: {self.total_money:,} so'm"
