from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.serialization import load_pem_private_key
from cryptography.exceptions import InvalidSignature

# Load private key from file
def load_private_key():
    with open("private_key.pem", "rb") as f:
        return load_pem_private_key(f.read(), password=None)

# Sign a message
def sign_message(message):
    private_key = load_private_key()
    signature = private_key.sign(
        message,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    return signature

# Verify a signature
def verify_signature(message, signature):
    try:
        public_key = load_private_key().public_key()
        public_key.verify(
            signature,
            message,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        print("✅ Signature Verified Successfully!")
    except InvalidSignature:
        print("❌ Signature Verification Failed!")