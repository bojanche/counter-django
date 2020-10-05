from channels.generic.websocket import WebsocketConsumer


class CountConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data=None):
        message = 'Bojan Websocket'
        self.send(text_data=message)
