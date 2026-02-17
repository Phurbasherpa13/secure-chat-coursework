import asyncio
import threading
import websockets
from security import SecurityEngine

class ChatCore:
    def __init__(self, log_callback, connected_callback, disconnected_callback):
        self.log = log_callback
        self.on_connected = connected_callback
        self.on_disconnected = disconnected_callback
        self.websocket = None
        self.loop = None
        self.security = None
        self.running = False

    def set_security(self, password):
        self.security = SecurityEngine(password)

    def start_thread(self):
        self.running = True
        self.thread = threading.Thread(target=self.run_loop, daemon=True)
        self.thread.start()

    def run_loop():
        pass

    async def host_server(self, host, port):
        pass

    async def handle_connection(self, websocket):
        pass

    async def connect_client(self, uri):
        pass

    def send(self, message):
        pass


    def stop(self):
        pass