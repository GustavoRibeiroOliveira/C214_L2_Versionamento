from app.encryption import Encryptor


def main():
    print("Encryptor")
    encryptor = Encryptor()

    text = "Text to be encrypted"

    encrypted_text = encryptor.encrypt(text, encryptor.key.decode())
    decrypted_text = encryptor.decrypt(encrypted_text, encryptor.key.decode())

    print(f"Text: {decrypted_text}")
    print(f"Encrypted Text: {encrypted_text}")

    while True:
        pass


if __name__ == "__main__":
    main()
