#!/usr/bin/env python3
"""
Week 4: AES Block Cipher - All requirements
"""

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2
import time

def pad(data):
    pad_len = 16 - (len(data) % 16)
    return data + bytes([pad_len] * pad_len)

def unpad(data):
    pad_len = data[-1]
    return data[:-pad_len]

def aes_encrypt(plaintext, key):
    iv = get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(pad(plaintext))
    return iv + ciphertext

def aes_decrypt(ciphertext, key):
    iv = ciphertext[:16]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = unpad(cipher.decrypt(ciphertext[16:]))
    return plaintext

print("=" * 70)
print("WEEK 4: AES BLOCK CIPHER")
print("=" * 70)


print("\n[AES Key Generation]")
key = get_random_bytes(32)  # AES-256
print(f"  Algorithm: AES-256-CBC")
print(f"  Key size: {len(key)*8} bits")
print(f"  Key (hex): {key.hex()[:40]}...")
print(f"  Block size: 128 bits (16 bytes)")
print(f"  Mode: CBC (Cipher Block Chaining)")


print("\n[Encryption & Decryption]")
plaintext = b"Confidential: Project launch date is 2026-12-01"
print(f"  Plaintext: {plaintext}")

start = time.time()
ciphertext = aes_encrypt(plaintext, key)
encrypt_time = (time.time() - start) * 1000

print(f"  Ciphertext (hex): {ciphertext[:40].hex()}...")
print(f"  Ciphertext size: {len(ciphertext)} bytes")
print(f"  Encryption time: {encrypt_time:.2f} ms")

start = time.time()
decrypted = aes_decrypt(ciphertext, key)
decrypt_time = (time.time() - start) * 1000

print(f"  Decrypted: {decrypted}")
print(f"  Decryption time: {decrypt_time:.2f} ms")
print(f"  Status: {'✓ PASS' if plaintext == decrypted else '✗ FAIL'}")


print("\n[File Encryption Demo]")
original_size = len(plaintext)
encrypted_size = len(ciphertext)
overhead = encrypted_size - original_size
print(f"  Original size: {original_size} bytes")
print(f"  Encrypted size: {encrypted_size} bytes")
print(f"  Overhead: {overhead} bytes (IV + padding)")


print("\n[Performance Test]")
test_data = b"A" * 100000  # 100KB
start = time.time()
encrypted = aes_encrypt(test_data, key)
elapsed = (time.time() - start) * 1000
print(f"  Encrypted 100 KB in {elapsed:.2f} ms")
print(f"  Speed: {100/elapsed:.1f} MB/s")


print("\n[Security Features]")
print("  ✓ Random IV prevents identical plaintext patterns")
print("  ✓ CBC mode chains blocks for better security")
print("  ✓ PKCS7 padding handles non-16-byte data")
print("  ✓ AES-256 provides 256-bit security strength")

print("\n" + "=" * 70)
print("=" * 70)
