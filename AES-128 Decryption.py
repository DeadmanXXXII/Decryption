from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import base64

def decrypt_aes128(ciphertext, key, iv):
    # Ensure the key and IV are in bytes
    key = bytes.fromhex(key)
    iv = bytes.fromhex(iv)
    
    # Decode the base64 encoded ciphertext
    ciphertext = base64.b64decode(ciphertext)

    # Create an AES cipher object with the key and initialization vector
    cipher = AES.new(key, AES.MODE_CBC, iv)

    # Decrypt the ciphertext and remove padding
    plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
    
    return plaintext.decode('utf-8')

# Example usage
encrypted_text = 'Base64EncodedCipherText'
key = '16ByteHexadecimalKey'  # 128-bit key in hex format
iv = '16ByteHexadecimalIV'  # 128-bit IV in hex format

decrypted_text = decrypt_aes128(encrypted_text, key, iv)
print(f'Decrypted text: {decrypted_text}')