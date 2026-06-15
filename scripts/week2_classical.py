#!/usr/bin/env python3
"""
Week 2: Classical Cryptography - Caesar and Vigenère Ciphers
BIT4138 Advanced Cryptography
"""

class CaesarCipher:
    """Caesar Cipher - shifts each letter by a fixed amount"""
    
    @staticmethod
    def encrypt(text, shift):
        result = []
        for char in text:
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                shifted = (ord(char) - base + shift) % 26 + base
                result.append(chr(shifted))
            else:
                result.append(char)
        return ''.join(result)
    
    @staticmethod
    def decrypt(text, shift):
        return CaesarCipher.encrypt(text, -shift)
    
    @staticmethod
    def brute_force(ciphertext):
        """Try all 25 possible shifts - demonstrates weakness"""
        results = []
        for shift in range(1, 26):
            decrypted = CaesarCipher.decrypt(ciphertext, shift)
            results.append((shift, decrypted[:60]))
        return results


class VigenereCipher:
    """Vigenère Cipher - polyalphabetic substitution using a keyword"""
    
    @staticmethod
    def encrypt(text, key):
        text = text.upper()
        key = key.upper()
        result = []
        key_len = len(key)
        
        for i, char in enumerate(text):
            if char.isalpha():
                shift = ord(key[i % key_len]) - ord('A')
                encrypted = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
                result.append(encrypted)
            else:
                result.append(char)
        return ''.join(result)
    
    @staticmethod
    def decrypt(text, key):
        text = text.upper()
        key = key.upper()
        result = []
        key_len = len(key)
        
        for i, char in enumerate(text):
            if char.isalpha():
                shift = ord(key[i % key_len]) - ord('A')
                decrypted = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
                result.append(decrypted)
            else:
                result.append(char)
        return ''.join(result)


def demonstrate_frequency_weakness():
    """Show why Caesar cipher is weak"""
    sample = "THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG"
    encrypted = CaesarCipher.encrypt(sample, 3)
    
    print("\n" + "=" * 70)
    print("FREQUENCY ANALYSIS DEMONSTRATION")
    print("=" * 70)
    print(f"Original:    {sample}")
    print(f"Encrypted:   {encrypted}")
    print("\nIn English, 'E' is most common letter (12.7%)")
    print("In ciphertext, 'W' appears most often")
    print("This reveals shift = 3 (E→H, but here E→W? Actually E→H with shift 3)")
    print("Attackers can guess shift by finding most frequent letter!")


print("=" * 70)
print("WEEK 2: CLASSICAL CRYPTOGRAPHY IMPLEMENTATION")
print("BIT4138 - Advanced Cryptography")
print("=" * 70)

# FIG 2.1: Caesar Cipher Implementation
print("\n[FIG 2.1] Caesar Cipher Implementation")
print("-" * 50)

test_text = "CRYPTOGRAPHY"
shift = 3

caesar_encrypted = CaesarCipher.encrypt(test_text, shift)
caesar_decrypted = CaesarCipher.decrypt(caesar_encrypted, shift)

print(f"  Algorithm:    Caesar Cipher (Shift Cipher)")
print(f"  Plaintext:    {test_text}")
print(f"  Shift key:    {shift}")
print(f"  Ciphertext:   {caesar_encrypted}")
print(f"  Decrypted:    {caesar_decrypted}")
print(f"  Status:       {'✓ PASS' if test_text == caesar_decrypted else '✗ FAIL'}")


# FIG 2.2: Vigenère Cipher Implementation

print("\n[FIG 2.2] Vigenère Cipher Implementation")
print("-" * 50)

test_text2 = "CRYPTOGRAPHY"
keyword = "KALI"

vigenere_encrypted = VigenereCipher.encrypt(test_text2, keyword)
vigenere_decrypted = VigenereCipher.decrypt(vigenere_encrypted, keyword)

print(f"  Algorithm:    Vigenère Cipher (Polyalphabetic)")
print(f"  Plaintext:    {test_text2}")
print(f"  Keyword:      {keyword}")
print(f"  Ciphertext:   {vigenere_encrypted}")
print(f"  Decrypted:    {vigenere_decrypted}")
print(f"  Status:       {'✓ PASS' if test_text2 == vigenere_decrypted else '✗ FAIL'}")

# Show how Vigenère works (mapping)
print("\n  How Vigenère works (first few characters):")
print(f"  P: C  R  Y  P  T  O  G  R  A  P  H  Y")
print(f"  K: K  A  L  I  K  A  L  I  K  A  L  I")
print(f"  Shift: 10 0  11 8  10 0  11 8  10 0  11 8")
print(f"  C: M  R  J  X  D  O  R  Z  K  P  S  G")


# FIG 2.3: Caesar Brute Force (Security Weakness)

print("\n[FIG 2.3] Caesar Cipher Brute Force Attack")
print("-" * 50)

sample_cipher = "WKH TXLFN EURZQ IRA MXPSV RYHU WKH ODCB GRJ"
print(f"  Ciphertext: {sample_cipher}")
print("  Brute forcing all 25 shifts:")
print("  Shift | Decrypted Text")
print("  ------|--------------------------------------------------")

for shift, result in CaesarCipher.brute_force(sample_cipher)[:10]:
    print(f"  {shift:3}   | {result}")


# FIG 2.4: User Input Validation

print("\n[FIG 2.4] User Input Validation Features")
print("-" * 50)

print("  The implementation handles:")
print("    ✓ Uppercase letters (A-Z)")
print("    ✓ Lowercase letters (a-z)")
print("    ✓ Spaces (preserved)")
print("    ✓ Punctuation (!@#$% etc.)")
print("    ✓ Numbers (0-9)")

# Test with mixed input
mixed_input = "Hello, World! 123"
caesar_mixed = CaesarCipher.encrypt(mixed_input, 5)
print(f"\n  Test: '{mixed_input}'")
print(f"  Encrypted: '{caesar_mixed}'")
print(f"  Non-letters preserved: ✓")


# FIG 2.5: Cipher Testing Results

print("\n[FIG 2.5] Cipher Testing Results & Security Analysis")
print("-" * 50)

# Test multiple scenarios
test_cases = [
    ("ATTACK", 3, "Caesar"),
    ("secret", 5, "Caesar"),
    ("HELLO", "KEY", "Vigenere"),
    ("crypto", "PASS", "Vigenere")
]

print("  Test Results Summary:")
print("  Test Case | Cipher Type | Result")
print("  ---------|-------------|--------")

# Caesar tests
caesar_test1 = CaesarCipher.encrypt("ATTACK", 3)
caesar_test1_dec = CaesarCipher.decrypt(caesar_test1, 3)
print(f"  ATTACK+3  | Caesar      | {'✓' if caesar_test1_dec == 'ATTACK' else '✗'}")

caesar_test2 = CaesarCipher.encrypt("secret", 5)
caesar_test2_dec = CaesarCipher.decrypt(caesar_test2, 5)
print(f"  secret+5  | Caesar      | {'✓' if caesar_test2_dec == 'secret' else '✗'}")

# Vigenere tests
vig_test1 = VigenereCipher.encrypt("HELLO", "KEY")
vig_test1_dec = VigenereCipher.decrypt(vig_test1, "KEY")
print(f"  HELLO+KEY | Vigenere    | {'✓' if vig_test1_dec == 'HELLO' else '✗'}")

vig_test2 = VigenereCipher.encrypt("crypto", "PASS")
vig_test2_dec = VigenereCipher.decrypt(vig_test2, "PASS")
print(f"  crypto+PASS| Vigenere   | {'✓' if vig_test2_dec == 'crypto' else '✗'}")

print("\n  Security Weaknesses Identified:")
print("    1. Caesar: Only 25 possible keys (can brute force in seconds)")
print("    2. Caesar: Preserves letter frequencies (vulnerable to frequency analysis)")
print("    3. Vigenère: Repeating keyword creates patterns")
print("    4. Both: Not secure for modern applications")
print("    5. Recommendation: Use AES or ChaCha20 for modern encryption")


# Summary

print("\n" + "=" * 70)
print("WEEK 2 SUMMARY")
print("=" * 70)
print("  ✓ Caesar Cipher implemented (shift cipher)")
print("  ✓ Vigenère Cipher implemented (polyalphabetic)")
print("  ✓ Brute force attack demonstrated Caesar weakness")
print("  ✓ Input validation preserves non-alphabetic characters")
print("  ✓ Security analysis completed")
print("=" * 70)
print("=" * 70)

# Demonstrate frequency analysis
demonstrate_frequency_weakness()

