import asyncio
import json
from channels.generic.websocket import WebsocketConsumer
from channels.consumer import AsyncConsumer


class CountConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        print("Connected ")
        await self.send({
            "type": "websocket.accept"
        })
        # await asyncio.sleep(10)
        # print("Sacu te zatvorim")
        # await self.send({
        #     "type": "websocket.close"
        # })
        await self.send({
            "type": "websocket.send",
            "text": "Hello world"
        })

    async def websocket_disconnect(self, event):
        print("Disconnected ", event)
        # await self.send({
        #     "type": "websocket.close"
        #     })

    async def websocket_receive(self, event):
        message = 'Bojan Websocket'
        self.send(message)
