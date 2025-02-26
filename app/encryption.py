from cryptography.fernet import Fernet


class Encryptor:
    def __init__(self):
        self.key = Fernet.generate_key()
        self.cipher = Fernet(self.key)

    def encrypt(self, text, key):
        cipher = Fernet(key.encode())
        return cipher.encrypt(text.encode()).decode()

    def decrypt(self, text, key):
        cipher = Fernet(key.encode())
        return cipher.decrypt(text.encode()).decode()
