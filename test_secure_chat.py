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

    def test_key_derivation_consistency(self):
        """Test that the same password generates the same key."""
        engine2 = security.SecurityEngine(self.password)
        
        # Both engines should have the same internal key
        self.assertEqual(self.engine.key, engine2.key)

    def test_decryption_with_wrong_key_fails(self):
        """Test that a message encrypted with Key A cannot be decrypted with Key B."""
        # Encrypt with Engine A
        encrypted_bytes = self.engine.encrypt_message(self.test_message)
        
        # Create Engine B with a DIFFERENT password
        wrong_engine = security.SecurityEngine("WrongPassword")
        
        # Try to decrypt with Engine B
        result = wrong_engine.decrypt_message(encrypted_bytes)
        
        # It should return the error string defined in your code
        self.assertEqual(result, "[Error: Decryption Failed]")

    def test_key_is_url_safe_base64(self):
        """Test that the generated key is in the correct format for Fernet."""
        # Fernet requires a 32-byte url-safe base64-encoded key.
        # Base64 encoding of 32 bytes results in 44 characters.
        self.assertEqual(len(self.engine.key), 44)

class TestFileUtils(unittest.TestCase):
    def setUp(self):
        """Create a temporary directory for test files."""
        self.test_dir = tempfile.mkdtemp()
        self.test_file = os.path.join(self.test_dir, "test_history.txt")
    
    def tearDown(self):
        """Remove the temporary directory after tests."""
        shutil.rmtree(self.test_dir)

    def test_save_and_load_history(self):
        """Test that saving a message and loading it back returns the same data."""
        message = "[2024-01-01 12:00:00] [System] Test started."
        
        # Save the message
        utils.save_to_file(self.test_file, message)
        
        # Load the message
        content = utils.load_history(self.test_file)
        
        # Verify content matches
        self.assertIn(message, content)
        
if __name__ == '__main__':
    unittest.main()