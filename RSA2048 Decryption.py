import os
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric.padding import PKCS1v15

def rsa_decrypt(encrypted_data, private_key):
    # Load the private key
    private_key = serialization.load_pem_private_key(private_key, password=None)

    # Decrypt the data
    decrypted_data = private_key.decrypt(
        encrypted_data,
        PKCS1v15(),
    )

    return decrypted_data

if __name__ == '__main__':
    # Replace these with your own values
    encrypted_data = b'\x01\x02\x03\x04...'  # Replace with the encrypted data
    private_key = b'-----BEGIN RSA PRIVATE KEY-----\n'  # Replace with the private key

    decrypted_data = rsa_decrypt(encrypted_data, private_key)

    print(decrypted_data.decode('utf-8'))