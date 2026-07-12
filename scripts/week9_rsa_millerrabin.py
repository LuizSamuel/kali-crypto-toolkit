#!/usr/bin/env python3
"""
Week 9: RSA Cryptosystem, Miller-Rabin Primality Test & Pollard Rho
BIT4138 - Advanced Cryptography
"""

import random
import hashlib

print("=" * 70)
print("WEEK 9: RSA CRYPTOSYSTEM, MILLER-RABIN & POLLARD RHO")
print("=" * 70)

# ============================================================
# PART 1: MILLER-RABIN PRIMALITY TEST
# ============================================================
print("\n[1] MILLER-RABIN PRIMALITY TEST")
print("-" * 50)

def miller_rabin(n, k=5):
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False
    
    d = n - 1
    r = 0
    while d % 2 == 0:
        d //= 2
        r += 1
    
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

test_numbers = [2, 3, 4, 5, 7, 11, 13, 17, 19, 23]
print("  Testing primality of numbers:")
print("  Number | Result")
print("  --------|---------")
for num in test_numbers:
    result = "Prime" if miller_rabin(num) else "Composite"
    print(f"  {num:6} | {result}")

print("\n  Testing 10 random numbers:")
print("  Number | Result")
print("  --------|---------")
for _ in range(10):
    num = random.randint(2, 1000)
    result = "Prime" if miller_rabin(num) else "Composite"
    print(f"  {num:6} | {result}")

# ============================================================
# PART 2: RSA KEY GENERATION
# ============================================================
print("\n[2] RSA KEY GENERATION")
print("-" * 50)

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def mod_inverse(e, phi):
    d = 0
    x1 = 0
    x2 = 1
    y1 = 1
    temp_phi = phi
    
    while e > 0:
        temp1 = temp_phi // e
        temp2 = temp_phi - temp1 * e
        temp_phi = e
        e = temp2
        x = x2 - temp1 * x1
        y = d - temp1 * y1
        x2 = x1
        x1 = x
        d = y1
        y1 = y
    
    if temp_phi == 1:
        return d + phi

p = 61
q = 53
print(f"  Prime p: {p}")
print(f"  Prime q: {q}")

n = p * q
phi = (p - 1) * (q - 1)
print(f"  Modulus n: {n}")
print(f"  Totient phi: {phi}")

e = 17
while gcd(e, phi) != 1:
    e += 2
print(f"  Public exponent e: {e}")

d = mod_inverse(e, phi)
print(f"  Private exponent d: {d}")

print(f"\n  Public Key: (e={e}, n={n})")
print(f"  Private Key: (d={d}, n={n})")

# ============================================================
# PART 3: RSA ENCRYPTION & DECRYPTION
# ============================================================
print("\n[3] RSA ENCRYPTION & DECRYPTION")
print("-" * 50)

message = "HELLO"
print(f"  Original Message: {message}")

ascii_values = [ord(char) for char in message]
print(f"  ASCII Values: {ascii_values}")

encrypted = [pow(char, e, n) for char in ascii_values]
print(f"  Encrypted (ciphertext): {encrypted}")

decrypted = [pow(char, d, n) for char in encrypted]
print(f"  Decrypted ASCII: {decrypted}")

decrypted_message = ''.join(chr(val) for val in decrypted)
print(f"  Decrypted Message: {decrypted_message}")
print(f"  Status: {'SUCCESS' if message == decrypted_message else 'FAIL'}")

# ============================================================
# PART 4: DIGITAL SIGNATURE
# ============================================================
print("\n[4] RSA DIGITAL SIGNATURE")
print("-" * 50)

hash_value = hashlib.sha256(message.encode()).hexdigest()
print(f"  Message: {message}")
print(f"  SHA-256 Hash: {hash_value[:40]}...")

hash_int = int(hash_value[:8], 16)
signature = pow(hash_int, d, n)
print(f"  Digital Signature: {signature}")

recovered_hash_int = pow(signature, e, n)
print(f"  Recovered Hash: {recovered_hash_int}")
print(f"  Original Hash: {hash_int}")
print(f"  Signature Status: {'VALID' if recovered_hash_int == hash_int else 'INVALID'}")

# ============================================================
# PART 5: POLLARD RHO FACTORIZATION
# ============================================================
print("\n[5] POLLARD RHO FACTORIZATION")
print("-" * 50)

def pollard_rho(n):
    if n % 2 == 0:
        return 2
    if n % 3 == 0:
        return 3
    
    x = random.randint(2, n - 2)
    y = x
    c = random.randint(1, n - 1)
    d = 1
    
    while d == 1:
        x = (pow(x, 2, n) + c) % n
        y = (pow(y, 2, n) + c) % n
        y = (pow(y, 2, n) + c) % n
        d = gcd(abs(x - y), n)
        
        if d == n:
            return None
    return d

test_n = 8051  # 83 * 97
print(f"  Factoring n = {test_n}")
factor = pollard_rho(test_n)
if factor:
    print(f"  Found factor: {factor}")
    print(f"  Other factor: {test_n // factor}")
else:
    print("  Factor not found")

# ============================================================
# SUMMARY
# ============================================================
print("\n" + "=" * 70)
print("WEEK 9 COMPLETE")
print("=" * 70)
