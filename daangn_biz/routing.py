# daangn_biz/routing.py
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from chat.token_auth import TokenAuthMiddlewareStack
import chat.routing

application = ProtocolTypeRouter({
    # (http->django views is added by default)
    'websocket': TokenAuthMiddlewareStack(
        URLRouter(
            chat.routing.websocket_urlpatterns
        )
    ),
})