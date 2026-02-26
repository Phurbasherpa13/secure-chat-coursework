# Secure Chat Application (Python-Based)

## Overview
A secure, real-time messaging application built with Python. This project demonstrartes End-to-End Encrpytion (E2EE) using AES-18, implemented via the Fernet module, over a WebSocket connection using Tkinter for the Gui

## Learning Outcomes
-  Learned to structure a complex application.
- Implemented real-world encryption standards. 
- Built a responsive, dark-themed interface.
- Understood file I/O operations.
- Utilize the threading module to isolate network logic.

## Features
- End-to-End encrpytion (E2EE)
- Real-time communication.
- Modular Code Structure.
- Chat History.
- Tamper Detection.
- User-friendly GUI.

## Project Structure
```SecureChatApp/
│
├── main.py              # Entry point
├── gui.py               # Tkinter GUi
├── core.py              # Network Layers and the event loop.
├── security.py          # Cryptography Layers.
├── utils.py             # Utility Layer (I/O) logs.
├── requirements.txt     # List of Python dependencies.
├── .gitignore          # Specifies files to exclude from version control.
└── README.md           # This file.
```
## Installation
## Prerequisites
- Python 3.8 or higher.
- Windows, macOS, or Linux.

## Quick Start
```bash
# Clone the repository
git clone https://github.com/Phurbasherpa13/secure-chat-coursework.git
cd secure-chat-coursework

# install the required libraries and modules
pip install -r requirements.txt

# run the application
python3 main.py
```

**Expected Output**
<img width="750" height="905" alt="image" src="https://github.com/user-attachments/assets/7b51fc6a-e722-44dc-8c67-04a682afc4ba" />


## Application Testing
```bash
python test_secure_chat.py
```

## License
This project is licensed under free MIT License. See more [License](/LICENSE).

## Author
- **Phurba Sherpa** - Intial work
