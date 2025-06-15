import json
from channels.generic.websocket import AsyncWebsocketConsumer

class InventoryConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Join the “inventory” group
        await self.channel_layer.group_add("inventory", self.channel_name)
        await self.accept()
        print("▶ WS CONNECTED:", self.channel_name)

    async def disconnect(self, code):
        await self.channel_layer.group_discard("inventory", self.channel_name)
        print("◀ WS DISCONNECTED:", code)

    # This method name “inventory_update” matches the “type” field we’ll send
    async def inventory_update(self, event):
        print("📣 WS EVENT:", event)
        await self.send(text_data=json.dumps({
            "message": event["message"]
        }))
