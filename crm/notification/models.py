from django.db import models
from product.models import Product
from inventory.models import Inventory

class Notification(models.Model):
    NOTIFICATION_TYPES = [
        (1, 'Simple Message'),
        (2, 'Min. Product Left'),
        (3, 'No Product Left')
    ]
    message = models.TextField(null=True, blank=True)
    notification_type = models.SmallIntegerField(choices=NOTIFICATION_TYPES, null=False, blank=False, default=1)
    product_id = models.ForeignKey('Product', on_delete=models.SET_NULL, null=False, blank=False)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    inventory_id = models.ManyToManyField('Inventory', related_name='notification_inventory')

    def __str__(self):
        return self.notification_type
