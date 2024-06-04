#Double bubble

from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import base64

def decrypt_aes256_double(ciphertext, key1, key2, iv):
    # Ensure the keys and IV are in bytes
    key1 = bytes.fromhex(key1)
    key2 = bytes.fromhex(key2)
    iv = bytes.fromhex(iv)
    
    # Decode the base64 encoded ciphertext
    ciphertext = base64.b64decode(ciphertext)

    # First layer of decryption
    cipher1 = AES.new(key1, AES.MODE_CBC, iv)
    intermediate = unpad(cipher1.decrypt(ciphertext), AES.block_size)
    
    # Second layer of decryption
    cipher2 = AES.new(key2, AES.MODE_CBC, iv)
    plaintext = unpad(cipher2.decrypt(intermediate), AES.block_size)
    
    return plaintext.decode('utf-8')

# Example usage
encrypted_text = 'Base64EncodedCipherText'
key1 = '32ByteHexadecimalKey1'  # 256-bit key in hex format
key2 = '32ByteHexadecimalKey2'  # Another 256-bit key in hex format
iv = '16ByteHexadecimalIV'  # 128-bit IV in hex format

decrypted_text = decrypt_aes256_double(encrypted_text, key1, key2, iv)
print(f'Decrypted text: {decrypted_text}')