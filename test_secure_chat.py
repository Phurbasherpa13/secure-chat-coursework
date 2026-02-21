import unittest
from cryptography.fernet import Fernet
from security_engine import SecurityEngine

class TestSecurityEngine(unittest.TestCase):
    def setUp(self):
        self.password = "my_secret_password"
        self.se = SecurityEngine(self.password)
        self.message = "Hello, World!"

    def test_init(self):
        self.assertIsInstance(self.se.cipher, Fernet)
        self.assertIsInstance(self.se.key, bytes)

    def test_generate_key_from_password(self):
        key1 = self.se._generate_key_from_password(self.password)
        key2 = self.se._generate_key_from_password(self.password)
        self.assertEqual(key1, key2)

        key3 = self.se._generate_key_from_password("other_password")
        self.assertNotEqual(key1, key3)

        self.assertEqual(len(key1), 44)

    def test_encrypt_message(self):
        encrypted = self.se.encrypt_message(self.message)
        self.assertIsInstance(encrypted, bytes)
        self.assertNotEqual(encrypted, self.message.encode('utf-8'))

    def test_decrypt_message(self):
        encrypted = self.se.encrypt_message(self.message)
        decrypted = self.se.decrypt_message(encrypted)
        self.assertEqual(decrypted, self.message)

    def test_decrypt_message_invalid_token(self):
        invalid_token = b'not_a_valid_token'
        decrypted = self.se.decrypt_message(invalid_token)
        self.assertEqual(decrypted, "[Error: Decryption Failed]")

    def test_cross_password_decryption(self):
        se1 = SecurityEngine("password1")
        se2 = SecurityEngine("password2")
        encrypted = se1.encrypt_message(self.message)
        decrypted = se2.decrypt_message(encrypted)
        self.assertEqual(decrypted, "[Error: Decryption Failed]")

if __name__ == '__main__':
    unittest.main()