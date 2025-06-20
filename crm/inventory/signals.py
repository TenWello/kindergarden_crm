from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from inventory.models import Inventory
from product.models   import Product
from ingredient.models import Ingredient

channel_layer = get_channel_layer()

def broadcast(msg):
    async_to_sync(channel_layer.group_send)(
        "inventory",
        {"type": "inventory_update", "message": msg}
    )

@receiver(post_save, sender=Inventory)
def inv_saved(sender, instance, created, **kwargs):
    action = "created" if created else "updated"
    broadcast(f"Inventory {action}: {instance.name}")

@receiver(post_delete, sender=Inventory)
def inv_deleted(sender, instance, **kwargs):
    broadcast(f"Inventory deleted: {instance.name}")

@receiver(post_save, sender=Product)
def prod_saved(sender, instance, created, **kwargs):
    if created:
        Inventory.objects.create(name=instance.name, product=instance, quantity=instance.quantity or 0)
        broadcast(f"New product: {instance.name}")

@receiver(post_save, sender=Ingredient)
def ing_saved(sender, instance, created, **kwargs):
    broadcast(f"Ingredient {'added' if created else 'updated'}: {instance.name}")
