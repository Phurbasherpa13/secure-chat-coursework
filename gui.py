import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import asyncio
from core import ChatCore
from utils import save_to_file, load_history

class SecureChatApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Secure WebSocket Chat")
        self.root.geometry("600x700")
        self.root.configure(bg="#1e1e1e")
        self.log_file = "chat_history.txt"

        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.style.configure("TFrame", background="#1e1e1e")
        self.style.configure("TLabel", background="#1e1e1e", foreground="#00ff00", font=("Consolas", 10))
        self.style.configure("TButton", font=("Consolas", 10, "bold"), background="#00cc00")
        self.style.map("TButton", background=[("active", "#00ff00")])

        self.core = ChatCore(
            log_callback=self.log_to_chat,
            connected_callback=self.on_connected,
            disconnected_callback=self.on_disconnected
        )

        self.create_widgets()
        self.core.start_thread()
        self.load_history_to_ui()
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

    def create_widgets(self):
        ttk.Label(self.root, text=">> SECURE WEBSOCKET CHAT <<", font=("Consolas", 16, "bold")).pack(pady=10)
        
        config_frame = ttk.Frame(self.root)
        config_frame.pack(fill="x", padx=20)
        
        ttk.Label(config_frame, text="IP:").grid(row=0, column=0)
        self.ip_entry = ttk.Entry(config_frame, width=15)
        self.ip_entry.insert(0, "127.0.0.1")
        self.ip_entry.grid(row=0, column=1, padx=5)

        ttk.Label(config_frame, text="Port:").grid(row=0, column=2)
        self.port_entry = ttk.Entry(config_frame, width=8)
        self.port_entry.insert(0, "8765")
        self.port_entry.grid(row=0, column=3, padx=5)

        ttk.Label(config_frame, text="Key:").grid(row=1, column=0, pady=5)
        self.key_entry = ttk.Entry(config_frame, show="*", width=20)
        self.key_entry.insert(0, "MySecretKey")
        self.key_entry.grid(row=1, column=1, columnspan=3, pady=5)

        btn_frame = ttk.Frame(self.root)
        btn_frame.pack(pady=10)
        self.host_btn = ttk.Button(btn_frame, text="HOST (Server)", command=self.start_host)
        self.host_btn.pack(side="left", padx=5)
        self.conn_btn = ttk.Button(btn_frame, text="JOIN (Client)", command=self.start_client)
        self.conn_btn.pack(side="left", padx=5)

        self.chat_log = scrolledtext.ScrolledText(self.root, bg="black", fg="#00ff00", font=("Consolas", 10), state="disabled")
        self.chat_log.pack(fill="both", expand=True, padx=20)

        input_frame = ttk.Frame(self.root)
        input_frame.pack(fill="x", padx=20, pady=10)
        self.msg_entry = ttk.Entry(input_frame, font=("Consolas", 10))
        self.msg_entry.pack(side="left", fill="x", expand=True)
        self.msg_entry.bind("<Return>", lambda e: self.send())
        self.send_btn = ttk.Button(input_frame, text="SEND", command=self.send, state="disabled")
        self.send_btn.pack(side="right", padx=5)

    def load_history_to_ui(self):
        history = load_history(self.log_file)
        if history:
            self.chat_log.config(state="normal")
            self.chat_log.insert(tk.END, history)
            self.chat_log.see(tk.END)
            self.chat_log.config(state="disabled")

    def start_host(self):
        if not self.check_inputs(): return
        asyncio.run_coroutine_threadsafe(
            self.core.host_server(self.ip_entry.get(), int(self.port_entry.get())),
            self.core.loop
        )
        self.toggle_inputs(False)

    def start_client(self):
        if not self.check_inputs(): return
        uri = f"ws://{self.ip_entry.get()}:{self.port_entry.get()}"
        asyncio.run_coroutine_threadsafe(
            self.core.connect_client(uri),
            self.core.loop
        )
        self.toggle_inputs(False)

    def check_inputs(self):
        if not self.key_entry.get():
            messagebox.showerror("Error", "Encryption Key required")
            return False
        self.core.set_security(self.key_entry.get())
        return True

    def toggle_inputs(self, enable):
        state = "normal" if enable else "disabled"
        self.host_btn.config(state=state)
        self.conn_btn.config(state=state)
        self.send_btn.config(state=state if not enable else "disabled")
        self.ip_entry.config(state=state)
        self.port_entry.config(state=state)
        self.key_entry.config(state=state)

    def send(self):
        msg = self.msg_entry.get()
        if msg:
            self.core.send(msg)
            self.log_to_chat(f"[You] {msg}")
            self.msg_entry.delete(0, tk.END)

    def on_connected(self, msg):
        self.log_to_chat(f"[SYSTEM] {msg}")
        self.send_btn.config(state="normal")

    def on_disconnected(self):
        self.log_to_chat("[SYSTEM] Disconnected")
        self.toggle_inputs(True)
        self.send_btn.config(state="disabled")

    def log_to_chat(self, msg):
        save_to_file(self.log_file, msg)
        def update():
            self.chat_log.config(state="normal")
            self.chat_log.insert(tk.END, msg + "\n")
            self.chat_log.see(tk.END)
            self.chat_log.config(state="disabled")
        self.root.after(0, update)

    def on_close(self):
        self.core.stop()
        self.root.destroy()