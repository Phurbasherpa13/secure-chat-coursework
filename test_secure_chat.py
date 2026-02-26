import unittest
from cryptography.fernet import Fernet
from security_engine import SecurityEngine

class TestSecurityEngine(unittest.TestCase):
    def setUp(self):
        """Setup a security engine for testing."""
        self.password = "MySecretPassword123"
        self.engine = security.SecurityEngine(self.password)
        self.test_message = "Hello, this is a secret message!"

    def test_encryption_decryption_cycle(self):
        """Test that a message can be encrypted and then decrypted correctly."""
        # Encrypt the message
        encrypted_bytes = self.engine.encrypt_message(self.test_message)
        
        # Ensure the encrypted data is not the same as the original
        self.assertNotEqual(encrypted_bytes, self.test_message.encode('utf-8'))
        
        # Decrypt the message
        decrypted_text = self.engine.decrypt_message(encrypted_bytes)
        
        # Check if decrypted text matches original
        self.assertEqual(decrypted_text, self.test_message)


if __name__ == '__main__':
    unittest.main()