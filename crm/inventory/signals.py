from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from product.models import Product
from ingredient.models import Ingredient
from inventory.models import Inventory

channel_layer = get_channel_layer()

def broadcast(msg):
    async_to_sync(channel_layer.group_send)(
        "inventory",
        { "type": "inventory_update", "message": msg }
    )

# When inventory entries change
@receiver(post_save, sender=Inventory)
def inv_saved(sender, instance, created, **kwargs):
    broadcast(f"Inventory {'created' if created else 'updated'}: {instance.name}")

@receiver(post_delete, sender=Inventory)
def inv_deleted(sender, instance, **kwargs):
    broadcast(f"Inventory deleted: {instance.name}")

# When products change (so inventory list should reflect new product imports)
@receiver(post_save, sender=Product)
def prod_saved(sender, instance, created, **kwargs):
    broadcast(f"Product {'added' if created else 'updated'}: {instance.name}")

@receiver(post_delete, sender=Product)
def prod_deleted(sender, instance, **kwargs):
    broadcast(f"Product removed: {instance.name}")

# Similarly for ingredients
@receiver(post_save, sender=Ingredient)
def ing_saved(sender, instance, created, **kwargs):
    broadcast(f"Ingredient {'added' if created else 'updated'}: {instance.name}")

@receiver(post_delete, sender=Ingredient)
def ing_deleted(sender, instance, **kwargs):
    broadcast(f"Ingredient removed: {instance.name}")
