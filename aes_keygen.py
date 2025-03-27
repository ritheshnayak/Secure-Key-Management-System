import os

def generate_aes_key():
    aes_key = os.urandom(32)  # 256-bit AES key
    with open("aes_key.bin", "wb") as f:
        f.write(aes_key)
    print("🔑 AES Key Generated and Saved to 'aes_key.bin'")