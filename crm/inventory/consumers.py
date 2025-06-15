import json
from channels.generic.websocket import AsyncWebsocketConsumer

class InventoryConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # join the “inventory” group
        await self.channel_layer.group_add("inventory", self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("inventory", self.channel_name)

    # called by our signal handlers
    async def inventory_update(self, event):
        # event["payload"] could be more detail if you like
        await self.send(text_data=json.dumps({
            "message": event["message"],
        }))
