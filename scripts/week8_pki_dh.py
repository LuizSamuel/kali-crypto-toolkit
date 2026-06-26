#!/usr/bin/env python3
"""
Week 8: PKI, Digital Certificates & Diffie-Hellman
BIT4138 - Advanced Cryptography
Student: Gakere Samuel
Admission: BSCCS/2024/55278
Lecturer: MR NYORO MICHAEL
"""

import hashlib
import time
import random

print("=" * 70)
print("WEEK 8: PKI, DIGITAL CERTIFICATES & DIFFIE-HELLMAN")
print("BIT4138 - Advanced Cryptography")
print("Student: Gakere Samuel")
print("Lecturer: MR NYORO MICHAEL")
print("=" * 70)

# ============================================================
# PART 1: DIFFIE-HELLMAN KEY EXCHANGE
# ============================================================
print("\n[1] DIFFIE-HELLMAN KEY EXCHANGE DEMONSTRATION")
print("-" * 50)

# Public parameters
p = 23  # Prime number
g = 5   # Generator

print(f"  Public Parameters:")
print(f"    Prime (p): {p}")
print(f"    Generator (g): {g}")

# Private keys (kept secret)
alice_private = 6
bob_private = 15

print(f"\n  Private Keys (Secret):")
print(f"    Alice's private key: {alice_private}")
print(f"    Bob's private key: {bob_private}")

# Public keys
alice_public = pow(g, alice_private, p)  # g^a mod p
bob_public = pow(g, bob_private, p)      # g^b mod p

print(f"\n  Public Keys (Exchanged):")
print(f"    Alice sends: {alice_public}")
print(f"    Bob sends: {bob_public}")

# Shared secrets
alice_secret = pow(bob_public, alice_private, p)  # B^a mod p
bob_secret = pow(alice_public, bob_private, p)    # A^b mod p

print(f"\n  Shared Secret:")
print(f"    Alice computes: {alice_secret}")
print(f"    Bob computes: {bob_secret}")
print(f"    Status: {'✓ MATCH - Secure key exchange successful' if alice_secret == bob_secret else '✗ MISMATCH'}")

# ============================================================
# PART 2: CERTIFICATE AUTHORITY AND CERTIFICATE STRUCTURE
# ============================================================
print("\n[2] X.509 CERTIFICATE STRUCTURE")
print("-" * 50)

print("  +--------------------------------------------------+")
print("  | X.509 DIGITAL CERTIFICATE                         |")
print("  +--------------------------------------------------+")
print("  | Version: 3                                        |")
print("  | Serial Number: 12:34:56:78:9A:BC                 |")
print("  | Signature Algorithm: sha256WithRSAEncryption     |")
print("  | Issuer: CN=DigiCert, O=DigiCert Inc, C=US       |")
print("  | Validity:                                         |")
print("  |   Not Before: 2026-01-01 00:00:00 GMT            |")
print("  |   Not After:  2027-01-01 23:59:59 GMT            |")
print("  | Subject: CN=example.com, O=Example Corp, C=KE    |")
print("  | Public Key Algorithm: RSA (2048 bits)            |")
print("  | Public Key: [hexadecimal representation]         |")
print("  | X509v3 Extensions:                               |")
print("  |   - Key Usage: Digital Signature, Key Encipher   |")
print("  |   - Extended Key Usage: TLS Server Auth          |")
print("  |   - Subject Alternative Name: DNS:example.com    |")
print("  | Signature: [CA's digital signature]               |")
print("  +--------------------------------------------------+")

# ============================================================
# PART 3: PKI COMPONENTS
# ============================================================
print("\n[3] PKI COMPONENTS AND THEIR ROLES")
print("-" * 50)

pki_components = {
    "Certificate Authority (CA)": "Trusted entity that issues and revokes certificates",
    "Registration Authority (RA)": "Verifies user identity and approves certificate requests",
    "Digital Certificate": "Binds public key to an identity",
    "Certificate Repository": "Stores and provides access to certificates",
    "End User": "Individual or system using certificates"
}

for component, role in pki_components.items():
    print(f"  {component}:")
    print(f"    {role}")

# ============================================================
# PART 4: CERTIFICATE LIFECYCLE
# ============================================================
print("\n[4] CERTIFICATE LIFECYCLE")
print("-" * 50)

lifecycle = [
    ("1", "Key Pair Generation", "User generates public/private key pair"),
    ("2", "Certificate Signing Request (CSR)", "User sends public key and identity to CA"),
    ("3", "Identity Verification", "CA verifies user identity"),
    ("4", "Certificate Issuance", "CA signs and issues certificate"),
    ("5", "Certificate Usage", "Certificate used for HTTPS, email, etc."),
    ("6", "Renewal or Revocation", "Certificate renewed before expiry or revoked")
]

print("  Step | Phase                  | Description")
print("  -----|------------------------|----------------------------------")
for step, phase, desc in lifecycle:
    print(f"  {step}    | {phase:<20} | {desc}")

# ============================================================
# PART 5: REVOCATION METHODS
# ============================================================
print("\n[5] CERTIFICATE REVOCATION METHODS")
print("-" * 50)

print("  CRL (Certificate Revocation List):")
print("    - List of revoked certificates published by CA")
print("    - Periodically downloaded by clients")
print("    - Can be delayed")

print("\n  OCSP (Online Certificate Status Protocol):")
print("    - Real-time certificate status checking")
print("    - Query sent to OCSP responder")
print("    - Immediate response")

# ============================================================
# PART 6: SSL/TLS HANDSHAKE
# ============================================================
print("\n[6] SSL/TLS HANDSHAKE WITH PKI")
print("-" * 50)

handshake_steps = [
    ("Client Hello", "Client sends supported ciphers and TLS version"),
    ("Server Hello", "Server selects cipher and sends random value"),
    ("Certificate", "Server sends digital certificate with public key"),
    ("Server Key Exchange", "DH or ECDHE parameters (if needed)"),
    ("Certificate Request", "Server requests client certificate (optional)"),
    ("Server Hello Done", "Server indicates end of handshake messages"),
    ("Client Key Exchange", "Client sends premaster secret"),
    ("Change Cipher Spec", "Both parties switch to negotiated cipher"),
    ("Finished", "Both parties verify handshake integrity")
]

print("  Phase                  | Description")
print("  -----------------------|----------------------------------")
for phase, desc in handshake_steps:
    print(f"  {phase:<22} | {desc}")

# ============================================================
# PART 7: SECURITY COMPARISON
# ============================================================
print("\n[7] SYMMETRIC VS ASYMMETRIC COMPARISON")
print("-" * 50)

print("  +------------------+--------------------+--------------------+")
print("  | Feature          | Symmetric          | Asymmetric         |")
print("  +------------------+--------------------+--------------------+")
print("  | Number of Keys   | 1 (shared)         | 2 (public/private) |")
print("  | Speed            | Fast              | Slow               |")
print("  | Key Distribution | Difficult         | Easy               |")
print("  | Scalability      | Low               | High               |")
print("  | Examples         | AES, DES, 3DES    | RSA, DH, ECC       |")
print("  | Use Case         | Bulk encryption   | Key exchange, Sign |")
print("  +------------------+--------------------+--------------------+")

# ============================================================
# PART 8: DISCRETE LOGARITHM PROBLEM
# ============================================================
print("\n[8] DISCRETE LOGARITHM PROBLEM EXPLANATION")
print("-" * 50)

print("  The security of Diffie-Hellman relies on the Discrete Logarithm Problem:")
print("")
print("  Given:")
print("    p = prime number (public)")
print("    g = generator (public)")
print("    A = g^a mod p (public)")
print("")
print("  Find:")
print("    a = ? (private key)")
print("")
print("  This is computationally difficult for large prime numbers.")
print("  Difficulty increases exponentially with key size.")

# Demonstrate discrete log difficulty
small_p = 23
small_g = 5
small_a = 6
small_A = pow(small_g, small_a, small_p)

print(f"\n  Example (small numbers):")
print(f"    p = {small_p}, g = {small_g}")
print(f"    Given A = {small_A}, find a")
print(f"    Answer: a = {small_a} (easy to find with small numbers)")
print(f"    With 2048-bit primes, finding 'a' is infeasible")

# ============================================================
# SUMMARY
# ============================================================
print("\n" + "=" * 70)
print("WEEK 8 SUMMARY")
print("=" * 70)
print("  ✓ Diffie-Hellman key exchange implemented")
print("  ✓ X.509 certificate structure explained")
print("  ✓ PKI components identified (CA, RA, Certificates)")
print("  ✓ Certificate lifecycle documented")
print("  ✓ SSL/TLS handshake analyzed")
print("  ✓ Symmetric vs Asymmetric compared")
print("  ✓ Discrete Logarithm Problem understood")
print("=" * 70)
print("=" * 70)

