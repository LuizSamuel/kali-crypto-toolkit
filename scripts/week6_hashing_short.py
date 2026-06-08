#!/usr/bin/env python3
"""
Week 6: Hashing and Password Security - All requirements
"""

import hashlib
import os
import time

def hash_sha256(data):
    """Generate SHA-256 hash"""
    return hashlib.sha256(data.encode()).hexdigest()

def hash_with_pbkdf2(password, salt=None, iterations=100000):
    """Hash password with salt using PBKDF2"""
    if salt is None:
        salt = os.urandom(32)
    key = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, iterations)
    return salt.hex(), key.hex()

def verify_password(password, salt_hex, hash_hex):
    """Verify password against stored hash"""
    salt = bytes.fromhex(salt_hex)
    test_hash = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
    return test_hash.hex() == hash_hex

print("=" * 70)
print("WEEK 6: HASHING AND PASSWORD SECURITY")
print("=" * 70)

# Part 1: SHA-256 Hash
print("\n[SHA-256 Hash Function]")
message = "BIT4138 Advanced Cryptography"
hash_result = hash_sha256(message)
print(f"  Message: {message}")
print(f"  SHA-256: {hash_result}")
print(f"  Hash length: {len(hash_result)} chars (256 bits)")
print(f"  Property: One-way - cannot reverse to get original")

# Part 2: Password Hashing with Salt
print("\n[Password Hashing with Salt - PBKDF2]")
password = "MySecurePassword123"
salt1, hash1 = hash_with_pbkdf2(password)
salt2, hash2 = hash_with_pbkdf2(password)

print(f"  Password: {password}")
print(f"  Salt 1: {salt1[:32]}...")
print(f"  Hash 1: {hash1[:32]}...")
print(f"  Salt 2: {salt2[:32]}...")
print(f"  Hash 2: {hash2[:32]}...")
print(f"  Same password, different hashes: {'✓' if hash1 != hash2 else '✗'}")
print(f"  Reason: Different random salts produce different hashes")

# Part 3: Login Authentication Simulation
print("\n[Login Authentication Simulation]")
stored_salt, stored_hash = hash_with_pbkdf2("correct_password123")

# Correct password
result1 = verify_password("correct_password123", stored_salt, stored_hash)
print(f"  Login 'correct_password123': {'✓ ACCESS GRANTED' if result1 else '✗ ACCESS DENIED'}")

# Wrong password
result2 = verify_password("wrong_password", stored_salt, stored_hash)
print(f"  Login 'wrong_password': {'✓ ACCESS GRANTED' if result2 else '✗ ACCESS DENIED'}")

# Part 4: Security Analysis
print("\n[Security Analysis]")
print("  Why hashing is irreversible:")
print("    - Cryptographic hash functions are one-way")
print("    - Small changes produce completely different hashes")
print("    - Avalanche effect: 1-bit change changes ~50% of hash bits")
print("  Importance of salt:")
print("    - Prevents rainbow table attacks")
print("    - Same password → different hash per user")
print("  PBKDF2 iterations (100,000):")
print("    - Slows down brute-force attacks")
print("    - Tunable for future hardware improvements")

# Part 5: Password Strength Test
print("\n[Password Strength Test]")
weak_password = "password123"
strong_password = "X9#kL2$mQ7@vR4!"

weak_hash = hash_sha256(weak_password)
strong_hash = hash_sha256(strong_password)

print(f"  Weak password: {weak_password}")
print(f"    Hash: {weak_hash[:40]}...")
print(f"    Status: Easily cracked - dictionary attack")
print(f"  Strong password: {strong_password}")
print(f"    Hash: {strong_hash[:40]}...")
print(f"    Status: Secure - high entropy")

print("\n" + "=" * 70)
print("=" * 70)
