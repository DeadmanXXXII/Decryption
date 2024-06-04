import salsa20
import os

def salsa20_decrypt(file_path, key, nonce):
    with open(file_path, 'rb') as f:
        encrypted_data = f.read()

    decrypted_data = salsa20.decrypt(encrypted_data, key, nonce)

    with open(file_path, 'wb') as f:
        f.write(decrypted_data)

if __name__ == '__main__':
    # Replace these with your own values
    file_path = 'encrypted_file'
    key = b'\x00' * 256  # Replace with the actual key
    nonce = b'\x00' * 64  # Replace with the actual nonce

    salsa20_decrypt(file_path, key, nonce)