# Secure Key Management System

## Overview
The **Secure Key Management System** (KMS) is designed for cryptographic key handling, ensuring secure key generation, storage, revocation, and authentication. It supports both symmetric (AES) and asymmetric (RSA) encryption and includes functionalities like X.509 certificate management and digital signatures.

## Features
- **AES Key Generation**: Securely generate symmetric AES keys.
- **RSA Key Pair Generation**: Create RSA public-private key pairs.
- **X.509 Certificate Management**: Generate and manage digital certificates.
- **Key Revocation System**: Maintain a revocation list for compromised keys.
- **Authentication & Digital Signatures**: Sign and verify messages using RSA keys.
- **Key Revocation Management**: Check and remove key revocations.
- **User-Friendly CLI**: Interactive command-line interface for key operations.

## Project Structure
```
Secure-KMS/
│── aes_keygen.py          # Generates AES keys
│── rsagen.py              # Generates RSA key pairs
│── certificate_manager.py # Handles X.509 certificate creation
│── krl_manager.py         # Manages key revocation and tracking
│── authentication.py      # Handles signing and verification
│── main.py                # Main CLI interface for user interaction
│── README.md              # Project documentation
```
## Features
- **AES Key Generation**: Generate 256-bit symmetric keys for efficient encryption.
- **RSA Key Pair Generation**: Create RSA public-private key pairs for asymmetric encryption and digital signatures.
- **X.509 Certificate Management**: Issue and validate certificates using Public Key Infrastructure (PKI).
- **Key Revocation List (KRL)**: Track and manage revoked keys to prevent unauthorized access.
- **Diffie-Hellman Key Exchange**: Securely exchange symmetric keys between communicating parties.
- **Authentication & Signing**: Sign messages with RSA private keys and verify them using public keys.

## System Architecture and Design
1. **Overview of System Components**
   - Centralized Key Distribution for Symmetric Encryption.
   - Public Key Infrastructure (PKI) for Asymmetric Encryption.
   - Secure Key Exchange Using Diffie-Hellman.
   - Key Revocation System to handle compromised keys.

2. **System Workflow and Interactions**
   - **Key Generation**: Generate AES and RSA keys securely.
   - **Key Distribution**: Distribute AES keys encrypted with RSA public keys.
   - **Key Exchange**: Use Diffie-Hellman to derive shared secrets.
   - **Data Encryption/Decryption**: Encrypt data using AES and decrypt using the same key.
   - **Key Revocation**: Revoke compromised keys and notify clients.

3. **Architecture Diagram**
   A visual representation of the system includes:
   - Central Key Management Server.
   - PKI System managing certificates.
   - Clients requesting and using encryption keys.
   - Key Exchange Process using Diffie-Hellman.
   - Key Revocation Mechanism ensuring compromised keys are replaced.

## Code Implementation
This system securely manages AES and RSA keys, X.509 certificates, and key exchange mechanisms. It includes:
1. AES key generation & encryption.
2. RSA key pair generation & signing.
3. Secure key exchange using Diffie-Hellman.
4. Certificate management (X.509 certificates).
5. Key revocation management (KRL).
6. Authentication & authorization.

### Libraries Used
```
| Library       | Purpose                                      |
|---------------|----------------------------------------------|
| `cryptography`| Key generation, encryption, signing, certificates |
| `json`        | Storing key revocation lists                 |
| `os`          | File operations                              |
| `base64`      | Encoding & decoding keys                     |
| `datetime`    | Handling key expiration                      |
```
## Installation & Setup
### Prerequisites
Ensure you have the following installed:
- Python 3.8+
- `cryptography` library

### Install Dependencies
```python
pip install cryptography
```

## Usage Guide
### 1. Generate AES and RSA Keys
Run:
```sh
python aes_keygen.py
python rsagen.py
```
This generates `aes_key.bin`, `private_key.pem`, and `public_key.pem`, ensuring revoked keys are removed.

### 2. Revoke a Key
Run:
```sh
python krl_manager.py
```
Enter the filename (e.g., `private_key.pem`) to revoke it.

### 3. Check Key Revocation Status
Use `check_key_status()` in `krl_manager.py` to determine if a key is revoked.

### 4. Sign and Verify Data
Modify `authentication.py` to sign and verify messages using:
```sh
python authentication.py
```

### 5. Perform Diffie-Hellman Key Exchange
Generate a Diffie-Hellman key pair:
```sh
python key_ex.py
```
Compute a shared secret using a peer's public key:
```sh
python key_ex.py compute_shared_secret peer_public_key.pem
```

## Security Considerations
- **Protect Private Keys**: Store `private_key.pem` securely and restrict access.
- **Use Strong Key Sizes**: Default RSA key size is 2048 bits for enhanced security.
- **Regular Key Rotation**: Periodically generate new keys to maintain security.
- **Monitor Revoked Keys**: Ensure revoked keys are not used accidentally.
