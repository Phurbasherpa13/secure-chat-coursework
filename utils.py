import os
from datetime import datetime

def save_to_file(file_path, message):
    """Saves the log message to a text file with a timestamp."""
    try:
        timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
        with open(file_path, "a", encoding="utf-8") as f:
            f.write(f"{timestamp} {message}\n")
    except Exception as e:
        print(f"Error saving log: {e}")

def load_history(file_path):
    """Reads the log file and returns the content."""
    if os.path.exists(file_path):
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                return f.read()
        except Exception as e:
            print(f"Error loading history: {e}")
    return ""