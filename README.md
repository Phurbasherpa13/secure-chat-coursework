# Secure Chat Application (Python-Based)

## Overview
A secure, real-time messaging application built with Python. This project demonstrartes End-to-End Encrpytion (E2EE) using AES-18, implemented via the Fernet module, over a WebSocket connection using Tkinter for the Gui

## Learning Outcomes
[TODO: Add learning objectives from the project]
- 1
- 2
- 3
- 4

## Features
- 1. End-to-End encrpytion (E2EE)
- 2. Real-time communication.
- 3. Modular Code Structure.
- 4. Chat History.
- 5. Tamper Detection.
- 6. User-friendly GUI.

## Project Structure
```SecureChatApp/
│
├── main.py              # Entry point: Initializes the app and applies nest-asyncio.
├── gui.py               # UI Layer: Handles Tkinter widgets, layout, and user events.
├── core.py              # Network Layer: Manages WebSocket connections and the event loop.
├── security.py          # Cryptography Layer: Handles AES-128 encryption/decryption logic.
├── utils.py             # Utility Layer: Handles file I/O (saving/loading history).
├── requirements.txt     # List of Python dependencies.
├── .gitignore          # Specifies files to exclude from version control.
└── README.md           # This file.
```

## Quick Start
```bash
# Clone the repository
git clone
cd secure-chat-coursework

# install the required libraries and modules
pip install -r requirements.txt

# run the application
python3 main.py
```

**Expected Output**
[TODO: Add images of the application]

## Application Testing

## License
This project is licensed under free MIT License. See more [License](/LICENSE).

## Author
- **Phurba sherpa** - Intial work