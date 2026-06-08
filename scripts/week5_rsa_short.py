#!/usr/bin/env python3
"""
Week 5: RSA Public Key Cryptography - Short Version (Fixed)
One screenshot covering all requirements
"""

from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes, serialization
import time

print("=" * 70)
print("WEEK 5: RSA PUBLIC KEY CRYPTOGRAPHY")
print("=" * 70)

# RSA Key Pair Generation
print("\n[RSA Key Pair Generation]")
start = time.time()
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)
gen_time = (time.time() - start) * 1000

public_key = private_key.public_key()
print(f"  Algorithm: RSA")
print(f"  Key size: 2048 bits")
print(f"  Public exponent: 65537")
print(f"  Generation time: {gen_time:.2f} ms")

# Export public key for viewing
public_pem = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)
print(f"  Public key (first 60 chars): {public_pem[:60].decode()}...")

# Encryption with Public Key (FIXED - added label=None)
print("\n[Public Key Encryption]")
message = b"Secret meeting at 3pm in Lab 4B"
print(f"  Original: {message.decode()}")

start = time.time()
ciphertext = public_key.encrypt(
    message,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)
encrypt_time = (time.time() - start) * 1000
print(f"  Ciphertext (hex): {ciphertext.hex()[:50]}...")
print(f"  Ciphertext size: {len(ciphertext)} bytes")
print(f"  Encryption time: {encrypt_time:.2f} ms")

# Decryption with Private Key (FIXED - added label=None)
print("\n[Private Key Decryption]")
start = time.time()
decrypted = private_key.decrypt(
    ciphertext,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)
decrypt_time = (time.time() - start) * 1000
print(f"  Decrypted: {decrypted.decode()}")
print(f"  Decryption time: {decrypt_time:.2f} ms")
print(f"  Status: {'✓ PASS' if message == decrypted else '✗ FAIL'}")

# Security Comparison
print("\n[Security & Comparison]")
print(f"  Asymmetric vs Symmetric:")
print(f"    - RSA uses two keys (public/private)")
print(f"    - AES uses one key (symmetric)")
print(f"  Max message size (2048-bit): 190 bytes with OAEP")
print(f"  Security level: ~112 bits (equivalent to AES-112)")
print(f"  Use case: Key exchange, digital signatures, small data")

# Note on hybrid encryption
print("\n[Hybrid Encryption Note]")
print("  RSA is 100x slower than AES")
print("  Real systems: RSA for key exchange + AES for bulk data")

print("\n" + "=" * 70)
print("=" * 70)
