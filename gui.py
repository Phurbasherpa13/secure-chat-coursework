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

    def create_widgets(self):
        ttk.Label(self.root, text=">> SECURE WEBSOCKET CHAT <<").pack(pady=10)

        self.chat_log = scrolledtext.ScrolledText(self.root, state="disabled")
        self.chat_log.pack(fill="both", expand=True, padx=20)

        self.msg_entry = ttk.Entry(self.root)
        self.msg_entry.pack(fill="x", padx=20, pady=10)
        self.msg_entry.bind("<Return>", lambda e: self.send())

        self.send_btn = ttk.Button(self.root, text="SEND", command=self.send)
        self.send_btn.pack()
    

    def send(self):
        msg = self.msg_entry.get()
        if msg:
            self.core.send(msg)
            self.log_to_chat(f"[You] {msg}")
            self.msg_entry.delete(0, tk.END)

    def log_to_chat(self, msg):
        save_to_file(self.log_file, msg)

        def update():
            self.chat_log.config(state="normal")
            self.chat_log.insert(tk.END, msg + "\n")
            self.chat_log.see(tk.END)
            self.chat_log.config(state="disabled")

        self.root.after(0, update)

    def load_history(self):
        history = load_history(self.log_file)
        if history:
            self.chat_log.config(state="normal")
            self.chat_log.insert(tk.END, history)
            self.chat_log.config(state="disabled")

    def on_connected(self, msg):
        self.log_to_chat(f"[SYSTEM] {msg}")

    def on_disconnected(self):
        self.log_to_chat("[SYSTEM] Disconnected")

    def on_close(self):
        self.core.stop()
        self.root.destroy()