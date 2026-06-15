#!/usr/bin/env python3
"""
Week 7: Digital Signatures and Certificates - Short Version
One screenshot covering all requirements
"""

from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes, serialization
import time
from datetime import datetime

print("=" * 70)
print("WEEK 7: DIGITAL SIGNATURES AND CERTIFICATES")
print("BIT4138 - Advanced Cryptography")
print("Student: Gakere Samuel")
print("Lecturer: MR NYORO MICHAEL")
print("=" * 70)

# ============================================================
# 1. KEY PAIR GENERATION FOR SIGNING
# ============================================================
print("\n[1] DIGITAL SIGNATURE KEY PAIR GENERATION")
start = time.time()
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)
gen_time = (time.time() - start) * 1000

public_key = private_key.public_key()
print(f"  Algorithm: RSA-PSS with SHA-256")
print(f"  Key size: 2048 bits")
print(f"  Generation time: {gen_time:.2f} ms")
print(f"  Purpose: Authenticity + Integrity (not confidentiality)")

# ============================================================
# 2. CREATE AND SIGN A DOCUMENT
# ============================================================
print("\n[2] DIGITAL SIGNATURE GENERATION")
document = b"Official Contract: Payment of KES 500,000 to CryptoLab"
print(f"  Document: {document.decode()}")

start = time.time()
signature = private_key.sign(
    document,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)
sign_time = (time.time() - start) * 1000

print(f"  Signature (hex): {signature.hex()[:60]}...")
print(f"  Signature size: {len(signature)} bytes")
print(f"  Signing time: {sign_time:.2f} ms")

# ============================================================
# 3. VERIFY THE SIGNATURE
# ============================================================
print("\n[3] SIGNATURE VERIFICATION")
start = time.time()
try:
    public_key.verify(
        signature,
        document,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    verify_time = (time.time() - start) * 1000
    print(f"  Result: VALID SIGNATURE")
    print(f"  Verification time: {verify_time:.2f} ms")
    print(f"  Document integrity: INTACT")
    print(f"  Signer identity: CONFIRMED")
except Exception as e:
    print(f"  Result: INVALID SIGNATURE - {e}")

# ============================================================
# 4. TAMPERED DOCUMENT TEST
# ============================================================
print("\n[4] TAMPERED DOCUMENT DETECTION")
tampered_document = document + b" - UNAUTHORIZED ADDITION"
print(f"  Original document with tampering detected")

try:
    public_key.verify(signature, tampered_document,
                      padding.PSS(mgf=padding.MGF1(hashes.SHA256()),
                      salt_length=padding.PSS.MAX_LENGTH), hashes.SHA256())
    print(f"  Result: FAIL - Tampered document incorrectly verified")
except Exception as e:
    print(f"  Result: SUCCESS - Tampered document rejected")
    print(f"  Reason: {type(e).__name__} - Signature verification failed")

# ============================================================
# 5. CERTIFICATE STRUCTURE
# ============================================================
print("\n[5] X.509 CERTIFICATE STRUCTURE")
print("  +----------------------------------------------------+")
print("  | X.509 CERTIFICATE EXAMPLE                          |")
print("  +----------------------------------------------------+")
print("  | Version: 3                                         |")
print("  | Serial Number: 55:66:77:88                         |")
print("  | Signature Algorithm: sha256WithRSAEncryption      |")
print("  | Issuer: CN=KaliCA, O=Kali Linux, C=US            |")
print("  | Validity:                                          |")
print("  |   Not Before: 2026-06-01 00:00:00 GMT             |")
print("  |   Not After:  2027-06-01 00:00:00 GMT             |")
print("  | Subject: CN=Gakere Samuel, O=University, C=KE     |")
print("  | Public Key: RSA (2048 bits)                       |")
print("  | X509v3 Extensions:                                |")
print("  |   - Key Usage: Digital Signature, Key Encipherment|")
print("  |   - Extended Key Usage: TLS Client Authentication |")
print("  +----------------------------------------------------+")

# ============================================================
# 6. SECURITY SUMMARY
# ============================================================
print("\n[6] SECURITY PROPERTIES")
print("  Digital Signatures provide:")
print("    - AUTHENTICITY: Confirms signer's identity")
print("    - INTEGRITY: Detects any document tampering")
print("    - NON-REPUDIATION: Signer cannot deny signing")
print("")
print("  Real-world applications:")
print("    - Software distribution (code signing)")
print("    - Legal documents (digital contracts)")
print("    - Email security (S/MIME, PGP)")
print("    - TLS/SSL certificates")

print("\n" + "=" * 70)
print("=" * 70)
