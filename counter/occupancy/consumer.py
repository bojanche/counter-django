import asyncio
import json
from channels.generic.websocket import WebsocketConsumer
from channels.consumer import AsyncConsumer


class CountConsumer(AsyncConsumer):
    async def connect(self, event):
        print("Connected ", event)
        self.accept()

    async def disconnect(self, event):
        print("Disconnected ", event)
        pass

    async def receive(self, event):
        message = 'Bojan Websocket'
        self.send(message)
