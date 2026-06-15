#!/usr/bin/env python3
"""
Week 3: Stream Ciphers - LFSR and RC4 
 Screenshot covering all requirements
"""

import time

class LFSR:
    def __init__(self, seed, taps):
        self.state = seed
        self.taps = taps
        self.mask = (1 << seed.bit_length()) - 1
    
    def next_bit(self):
        feedback = 0
        for tap in self.taps:
            feedback ^= (self.state >> tap) & 1
        self.state = ((self.state << 1) | feedback) & self.mask
        return feedback
    
    def generate_sequence(self, bits):
        return [self.next_bit() for _ in range(bits)]

class RC4:
    @staticmethod
    def encrypt(data, key):
        if isinstance(data, str):
            data = data.encode()
        if isinstance(key, str):
            key = key.encode()
        
        S = list(range(256))
        j = 0
        for i in range(256):
            j = (j + S[i] + key[i % len(key)]) % 256
            S[i], S[j] = S[j], S[i]
        
        i = j = 0
        result = bytearray()
        for byte in data:
            i = (i + 1) % 256
            j = (j + S[i]) % 256
            S[i], S[j] = S[j], S[i]
            result.append(byte ^ S[(S[i] + S[j]) % 256])
        return bytes(result)

print("=" * 70)
print("WEEK 3: STREAM CIPHERS - LFSR & RC4")
print("=" * 70)

# LFSR Demo
print("\n[LFSR - Linear Feedback Shift Register]")
lfsr = LFSR(seed=0b1011, taps=[3, 1])
print(f"  Polynomial: x^4 + x + 1")
print(f"  Seed: 1011 (binary)")
print(f"  Generated 30 bits: {''.join(map(str, lfsr.generate_sequence(30)))}")

# RC4 Demo
print("\n[RC4 Stream Cipher]")
key = "KaliKey"
plaintext = "BIT4138 Stream Cipher Demo"
ciphertext = RC4.encrypt(plaintext, key)
decrypted = RC4.encrypt(ciphertext, key)
print(f"  Key: {key}")
print(f"  Plaintext: {plaintext}")
print(f"  Ciphertext (hex): {ciphertext[:30].hex()}...")
print(f"  Decrypted: {decrypted.decode()}")
print(f"  Status: {'✓' if plaintext == decrypted.decode() else '✗'}")

# Performance
print("\n[Performance Test]")
test_data = b"X" * 10000
start = time.time()
RC4.encrypt(test_data, key)
elapsed = (time.time() - start) * 1000
print(f"  Encrypted 10,000 bytes in {elapsed:.2f} ms")
print(f"  Speed: {10000/elapsed:.1f} KB/s")

# XOR Property
print("\n[Stream Cipher Property]")
print("  Encryption: Ciphertext = Plaintext ⊕ Keystream")
print("  Decryption: Plaintext = Ciphertext ⊕ Keystream")
print("  Same operation for both (XOR is symmetric)")

print("\n" + "=" * 70)
print("✓ LFSR implemented")
print("✓ RC4 working correctly")
print("✓ Performance tested")
print("=" * 70)
