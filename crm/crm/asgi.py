import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "crm.settings")
django_asgi_app = get_asgi_application()

# Debug print to ensure this file is loaded
print("🛠  ASGI application starting…")

import inventory.routing

application = ProtocolTypeRouter({
    "http": django_asgi_app,
    "websocket": AuthMiddlewareStack(
        URLRouter(inventory.routing.websocket_urlpatterns)
    ),
})
