

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chanel6.settings')

from channels.routing import ProtocolTypeRouter,URLRouter
from testapp import routing
from channels.auth import AuthMiddlewareStack

application = ProtocolTypeRouter({
    'http':get_asgi_application(),
    'websocket':AuthMiddlewareStack
    (URLRouter(
        routing.websocket_urlpatterns
    ))
}

)
# get_asgi_application()
