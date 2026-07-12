#!/usr/bin/env python3
"""
Week 10: ElGamal Cryptosystem & Elliptic Curve Cryptography (ECC)
BIT4138 - Advanced Cryptography
"""

import random
import time

print("=" * 70)
print("WEEK 10: ELGAMAL CRYPTOSYSTEM & ECC")
print("=" * 70)

# ============================================================
# PART 1: ELGAMAL KEY GENERATION
# ============================================================
print("\n[1] ELGAMAL KEY GENERATION")
print("-" * 50)

p_elgamal = 23
g_elgamal = 5
private_key = 6
public_key = pow(g_elgamal, private_key, p_elgamal)

print(f"  Prime p: {p_elgamal}")
print(f"  Generator g: {g_elgamal}")
print(f"  Private Key x: {private_key}")
print(f"  Public Key y: {public_key}")

# ============================================================
# PART 2: ELGAMAL ENCRYPTION
# ============================================================
print("\n[2] ELGAMAL ENCRYPTION")
print("-" * 50)

message_elgamal = 10
k = 7

c1 = pow(g_elgamal, k, p_elgamal)
c2 = (message_elgamal * pow(public_key, k, p_elgamal)) % p_elgamal

print(f"  Plaintext M: {message_elgamal}")
print(f"  Random k: {k}")
print(f"  Ciphertext C1: {c1}")
print(f"  Ciphertext C2: {c2}")

# ============================================================
# PART 3: ELGAMAL DECRYPTION
# ============================================================
print("\n[3] ELGAMAL DECRYPTION")
print("-" * 50)

decrypted_elgamal = (c2 * pow(c1, p_elgamal - 1 - private_key, p_elgamal)) % p_elgamal

print(f"  Recovered Plaintext: {decrypted_elgamal}")
print(f"  Status: {'SUCCESS' if decrypted_elgamal == message_elgamal else 'FAIL'}")

# ============================================================
# PART 4: RANDOMNESS DEMONSTRATION
# ============================================================
print("\n[4] ELGAMAL RANDOMNESS DEMONSTRATION")
print("-" * 50)

message_test = 15
print(f"  Original Message: {message_test}")
print("  Encryption with different random k values:")
print("  k | C1 | C2")
print("  ---|----|----")

for k_test in [3, 7, 11, 15, 19]:
    c1_test = pow(g_elgamal, k_test, p_elgamal)
    c2_test = (message_test * pow(public_key, k_test, p_elgamal)) % p_elgamal
    print(f"  {k_test:2} | {c1_test:2} | {c2_test:2}")

print("\n  Same plaintext produces different ciphertexts")

# ============================================================
# PART 5: RSA vs ELGAMAL BENCHMARK
# ============================================================
print("\n[5] RSA vs ELGAMAL BENCHMARK")
print("-" * 50)

# ElGamal timing
start = time.time()
for _ in range(100):
    pow(g_elgamal, k, p_elgamal)
elgamal_time = (time.time() - start) * 1000

# RSA timing (simulated with small numbers)
start = time.time()
for _ in range(100):
    pow(5, 17, 187)
rsa_time = (time.time() - start) * 1000

print(f"  ElGamal (100 operations): {elgamal_time:.4f} ms")
print(f"  RSA (100 operations): {rsa_time:.4f} ms")
print(f"  Note: RSA is faster for these small numbers")

# ============================================================
# PART 6: ECC DEMONSTRATION (CONCEPTUAL)
# ============================================================
print("\n[6] ELLIPTIC CURVE CRYPTOGRAPHY (ECC)")
print("-" * 50)

print("  Elliptic Curve Equation: y² = x³ + ax + b")
print("  Example: y² = x³ - 3x + 5")
print("")
print("  ECC Point Operations:")
print("    - Point Addition: P + Q = R")
print("    - Point Doubling: 2P = R")
print("    - Scalar Multiplication: kP = R")
print("")
print("  ECC Advantages:")
print("    - 256-bit ECC ≈ 3072-bit RSA security")
print("    - Faster computations")
print("    - Lower power consumption")
print("    - Suitable for IoT and mobile devices")
print("")
print("  ECC Applications:")
print("    - Mobile banking")
print("    - Smart cards")
print("    - Cryptocurrencies")
print("    - Secure messaging")

# ============================================================
# PART 7: ELGAMAL APPLICATIONS
# ============================================================
print("\n[7] ELGAMAL APPLICATIONS")
print("-" * 50)

print("  ElGamal is used in:")
print("    - Digital signatures (ElGamal signature scheme)")
print("    - Diffie-Hellman key exchange")
print("    - Encryption systems")
print("    - Secure email")
print("    - VPN authentication")
print("")
print("  Security Note:")
print("    - Security relies on Discrete Logarithm Problem")
print("    - Random k must be unique for each encryption")
print("    - Reusing k compromises security")

# ============================================================
# SUMMARY
# ============================================================
print("\n" + "=" * 70)
print("WEEK 10 COMPLETE")
print("=" * 70)
