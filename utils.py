# utils.py
import os
from datetime import datetime


def save_to_file(filename, message):
    try:
        timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
        with open(filename, "a", encoding="utf-8") as f:
            f.write(f"{timestamp} {message}\n")
    except Exception as e:
        print(f"Error saving log: {e}")


def load_history(filename):
    if os.path.exists(filename):
        try:
            with open(filename, "r", encoding="utf-8") as f:
                return f.read()
        except Exception as e:
            print(f"Error loading history: {e}")
    return ""
