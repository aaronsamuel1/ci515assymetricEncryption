#encryption with RSA library

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

def generate_keys():
    """Generate a pair of RSA keys. (public and private)"""
    key = RSA.generate(2048)
    private_key = key.export_key("PEM")
    public_key = key.publickey().export_key("PEM")
    return private_key, public_key

def encrypt_message(public_key, message):  
    """Encrypt a message using the public key."""
    public_key = RSA.import_key(public_key)
    cipher = PKCS1_OAEP.new(public_key)
    ciphertext = cipher.encrypt(message.encode('utf-8'))
    return ciphertext

def decrypt_message(private_key, ciphertext):
    """Decrypt a message using the private key."""
    private_key = RSA.import_key(private_key)
    cipher = PKCS1_OAEP.new(private_key)
    plaintext = cipher.decrypt(ciphertext).decode('utf-8')
    return plaintext 



if __name__ == "__main__":
    # Example usage
    private_key, public_key = generate_keys()
    message = "This is a secret message"
    ciphertext = encrypt_message( public_key, message)
    decrypted_message = decrypt_message( private_key, ciphertext)
    print("Original message:", message)
    print("Encrypted message:", ciphertext)
    print("Decrypted message:", decrypted_message)