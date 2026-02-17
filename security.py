import hashlib
import base64
from cryptography.fernet import Fernet, InvalidToken

class SecurityEngine:
    """Handles Encryption/Decryption using Fernet (AES-128)."""
    def __init__(self, password):
        self.key = self._generate_key_from_password(password)
        self.cipher = Fernet(self.key)

    def _generate_key_from_password(self, password):
        digest = hashlib.sha256(password.encode()).digest()
        return base64.urlsafe_b64encode(digest)

    def encrypt_message(self, message):
        return self.cipher.encrypt(message.encode('utf-8'))

    def decrypt_message(self, encrypted_bytes):
        try:
            return self.cipher.decrypt(encrypted_bytes).decode('utf-8')
        except InvalidToken:
            return "[Error: Decryption Failed]"