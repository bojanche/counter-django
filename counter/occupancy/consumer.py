import asyncio
import json
from channels.generic.websocket import WebsocketConsumer
from channels.consumer import AsyncConsumer
from channels.exceptions import StopConsumer
from channels.layers import get_channel_layer


class CountConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        print("Connected ")
        await self.send({
            "type": "websocket.accept"
        })
        while True:
            await asyncio.sleep(3)
            print("Entered loop")
            await self.send({
                "type": "websocket.send",
                "text": "Hello world"
            })


    async def websocket_disconnect(self, event):
        print("Disconnected ", event)
        await self.send({
            "type": "websocket.disconnect"
            })

        raise StopConsumer()


    async def websocket_receive(self, event):
        message = 'Bojan Websocket'
        print("*******Bojanov diskonektni event", event)
        await self.send(message)
