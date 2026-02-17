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

    def run_loop(self):
        self.loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self.loop)
        self.loop.run_forever()

    async def host_server(self, host, port):
        try:
            async with websockets.serve(self.handle_connection, host, port):
                self.log(f"[SYSTEM] Server started on ws://{host}:{port}")
                await asyncio.Future()
        except Exception as e:
            self.log(f"[Error] Server failed: {e}")
            self.on_disconnected()

    async def handle_connection(self, websocket):
        self.websocket = websocket
        self.on_connected("Client Connected")
        self.log("[SYSTEM] Secure connection established.")

        try:
            async for message in websocket:
                decrypted = self.security.decrypt_message(message)
                self.log(f"[Friend] {decrypted}")
        except websockets.exceptions.ConnectionClosed:
            self.log("[SYSTEM] Connection closed.")
        finally:
            self.on_disconnected()

    async def connect_client(self, uri):
        try:
            async with websockets.connect(uri) as websocket:
                self.websocket = websocket
                self.on_connected("Connected to Server")
                self.log(f"[SYSTEM] Connected to {uri}")

                async for message in websocket:
                    decrypted = self.security.decrypt_message(message)
                    self.log(f"[Friend] {decrypted}")
        except Exception as e:
            self.log(f"[Error] Connection failed: {e}")
            self.on_disconnected()

    def send(self, message):
        if not self.websocket or not self.security:
            return
        encrypted = self.security.encrypt_message(message)
        asyncio.run_coroutine_threadsafe(
            self.websocket.send(encrypted), self.loop
        )


    def stop(self):
        if self.loop:
            self.loop.call_soon_threadsafe(self.loop.stop)
        self.running = False