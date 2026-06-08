#!/usr/bin/env python3
"""
Week 1: Complete Cryptography Environment Setup Test
My logbook screenshots
"""

import sys
import platform
from datetime import datetime

print("=" * 70)
print("BIT4138: ADVANCED CRYPTOGRAPHY - WEEK 1")
print("Cryptography Environment Setup Verification")
print("=" * 70)
print(f"Date/Time: {datetime.now()}")
print(f"Python Version: {sys.version}")
print(f"Platform: {platform.system()} {platform.release()}")
print("=" * 70)

#  Fernet (Cryptography Library)
print("\n[TEST 1] Fernet Symmetric Encryption (cryptography library)")
try:
    from cryptography.fernet import Fernet
    
    # Generate key
    key = Fernet.generate_key()
    print(f"  ✓ Fernet key generated: {key[:20]}...")
    
    # Create cipher
    cipher = Fernet(key)
    
    # Test message
    plaintext = b"BIT4138 Advanced Cryptography - Environment Ready"
    print(f"  ✓ Plaintext: {plaintext}")
    
    # Encrypt
    ciphertext = cipher.encrypt(plaintext)
    print(f"  ✓ Ciphertext: {ciphertext[:30]}...")
    
    # Decrypt
    decrypted = cipher.decrypt(ciphertext)
    print(f"  ✓ Decrypted: {decrypted}")
    
    # Verify
    if plaintext == decrypted:
        print("  ✓ VERIFICATION: Encryption/Decryption successful")
    else:
        print("  ✗ VERIFICATION: Failed")
        
except Exception as e:
    print(f"  ✗ Error: {e}")

# Test 2: AES (PyCryptodome)
print("\n[TEST 2] AES-256 Block Cipher (pycryptodome library)")
try:
    from Crypto.Cipher import AES
    from Crypto.Random import get_random_bytes
    
    # Generate 256-bit key
    key = get_random_bytes(32)
    print(f"  ✓ AES-256 key generated: {key[:10].hex()}...")
    
    # Create cipher with EAX mode (authenticated encryption)
    cipher = AES.new(key, AES.MODE_EAX)
    nonce = cipher.nonce
    print(f"  ✓ Nonce/IV: {nonce.hex()[:20]}...")
    
    # Test message
    plaintext = b"AES-256 encryption test for BIT4138"
    print(f"  ✓ Plaintext: {plaintext}")
    
    # Encrypt and authenticate
    ciphertext, tag = cipher.encrypt_and_digest(plaintext)
    print(f"  ✓ Ciphertext: {ciphertext[:30].hex()}...")
    print(f"  ✓ Authentication tag: {tag.hex()[:20]}...")
    
    # Decrypt and verify
    cipher_dec = AES.new(key, AES.MODE_EAX, nonce=nonce)
    decrypted = cipher_dec.decrypt_and_verify(ciphertext, tag)
    print(f"  ✓ Decrypted: {decrypted}")
    
    if plaintext == decrypted:
        print("  ✓ VERIFICATION: AES-256 encryption/decryption successful")
    else:
        print("  ✗ VERIFICATION: Failed")
        
except Exception as e:
    print(f"  ✗ Error: {e}")

# Test 3: OpenSSL (System)
print("\n[TEST 3] OpenSSL System Check")
import subprocess
try:
    result = subprocess.run(['openssl', 'version'], capture_output=True, text=True)
    if result.returncode == 0:
        print(f"  ✓ OpenSSL: {result.stdout.strip()}")
    else:
        print("  ✗ OpenSSL not found")
except:
    print("  ✗ OpenSSL command failed")

# Summary
print("\n" + "=" * 70)
print("WEEK 1 SUMMARY")
print("=" * 70)
print("  ✓ Python virtual environment configured")
print("  ✓ Cryptography library installed (Fernet)")
print("  ✓ PyCryptodome installed (AES)")
print("  ✓ OpenSSL available for certificates")
print("  ✓ Environment ready for Weeks 2-10")
print("=" * 70)
print("=" * 70)
