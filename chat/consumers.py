from channels.consumer import AsyncConsumer


class EchoConsumer(AsyncConsumer):

    async def websocket_connect(self, event):
        self.user = self.scope["user"]
        await self.send({
            "type": "websocket.accept",
        })

    async def websocket_disconnect(self, event):
        await self.send({
            "type": "websocket.accept"
        })

    async def websocket_receive(self, event):
        await self.send({
            "type": "websocket.send",
            "text": str(self.user) + ': ' + event["text"],
        })

