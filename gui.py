# Imported Modules
import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import asyncio
from core import ChatCore
from utils import save_to_file, load_history

# This class handles the graphical interface of the application
class SecureChatApp:
    
    # This is the intializer function to intialize application heading information
    def __init__(self, root):
        self.root = root
        self.root.title("Secure WebSocket Chat")
        self.root.geometry("600x700")
        self.root.configure(bg="#1e1e1e")

        self.log_file = "chat_history.txt"

        self.core = ChatCore(
            log_callback=self.log_to_chat,
            connected_callback=self.on_connected,
            disconnected_callback=self.on_disconnected
        )

        self.create_widgets()
        self.core.start_thread()
        self.load_history()

        self.root.protocol("WM_DELETE_WINDOW", self.on_close)