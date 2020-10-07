import asyncio
import json
from channels.generic.websocket import WebsocketConsumer
from channels.consumer import AsyncConsumer


class CountConsumer(WebsocketConsumer):
    async def connect(self):
        print("Connected ")
        # await self.accept()
        await self.send({
            "type": "websocket.accept"
        })
        await asyncio.sleep(10)
        await self.send({
            "type": "websocket.close"
        })

    async def disconnect(self, event):
        print("Disconnected ", event)
        pass

    async def receive(self, event):
        message = 'Bojan Websocket'
        self.send(message)
