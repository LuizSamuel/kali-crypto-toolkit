cd ~/kali-crypto-toolkit/creative

sed -i 's/Lecturer: \[Lecturer Name\]/Lecturer: MR NYORO MICHAEL/g' 05_certificate.txt

# The  update of the certificate file directly
cat > creative/05_certificate.txt << 'CERT'
+----------------------------------------------------------------------+
|                                                                      |
|                    CERTIFICATE OF COMPLETION                         |
|                                                                      |
|                    BIT4138: Advanced Cryptography                    |
|                                                                      |
|                    Presented to: Gakere Samuel                       |
|                    Admission: BSCCS/2024/55278                       |
|                    Date: 2026                                        |
|                                                                      |
|                    -------------------------------------------------  |
|                    Completed Weeks 1-6                               |
|                    -------------------------------------------------  |
|                                                                      |
|     [X] Environment Setup    [X] Classical Ciphers    [X] Stream Ciphers |
|     [X] AES Block Cipher     [X] RSA Public Key       [X] Hashing & PWD |
|                                                                      |
|                                                                      |
|                    ------------- SIGNED -------------                |
|                                                                      |
|                    Lecturer: MR NYORO MICHAEL                        |
|                    Date: 2026                                        |
|                                                                      |
+----------------------------------------------------------------------+
CERT

# Update of the Python banner 
cat > creative/06_python_banner.py << 'PYTHON'
#!/usr/bin/env python3
"""
Custom Crypto Banner for BIT4138 Scripts
"""
def display_banner(week_num, title):
    banner = f"""
+----------------------------------------------------------------------+
|  BIT4138: ADVANCED CRYPTOGRAPHY                                      |
|  Week {week_num}: {title:<50} |
|  Student: Gakere Samuel                                             |
|  Admission: BSCCS/2024/55278                                        |
|  Lecturer: MR NYORO MICHAEL                                         |
+----------------------------------------------------------------------+
"""
    print(banner)

def display_footer():
    footer = """
+----------------------------------------------------------------------+
|  Cryptography is the art of protecting information                  |
|  BIT4138 - Advanced Cryptography - 2026                             |
|  Kali Linux - Cryptographic Toolkit                                 |
+----------------------------------------------------------------------+
"""
    print(footer)

if __name__ == "__main__":
    display_banner(1, "Environment Setup")
    print("  Creative work ready for your report.")
    display_footer()
PYTHON

# The update of the HTML comparison table
sed -i 's/BIT4138 Advanced Cryptography - 2026/BIT4138 Advanced Cryptography - 2026 | Lecturer: MR NYORO MICHAEL/g' creative/03_algorithm_comparison.html

# Creative summary
cat > creative/07_creative_summary.txt << 'SUMMARY'
+----------------------------------------------------------------------+
|                    CREATIVE WORK SUMMARY - BIT4138                   |
+----------------------------------------------------------------------+
|                                                                      |
|   Student: Gakere Samuel                                             |
|   Admission: BSCCS/2024/55278                                        |
|   Lecturer: MR NYORO MICHAEL                                         |
|   Course: BIT4138 - Advanced Cryptography                           |
|   Year: 2026                                                         |
|                                                                      |
+----------------------------------------------------------------------+
|                                                                      |
|   File 1: 01_cover_banner.txt     - ASCII Art Cover Page            |
|   File 2: 02_crypto_timeline.txt  - Learning Timeline               |
|   File 3: 03_algorithm_comparison.html - HTML Comparison Table      |
|   File 4: 04_crypto_cheatsheet.txt - Quick Reference Cheat Sheet    |
|   File 5: 05_certificate.txt      - Certificate of Completion       |
|   File 6: 06_python_banner.py     - Reusable Python Banner          |
|   File 7: 07_creative_summary.txt - This summary file               |
|                                                                      |
|   Location: ~/kali-crypto-toolkit/creative/                         |
|                                                                      |
+----------------------------------------------------------------------+
SUMMARY

# Making Python script executable
chmod +x creative/06_python_banner.py

# The updated certificate
echo ""
echo "+----------------------------------------------------------------------+"
echo "|                    UPDATED WITH LECTURER NAME                        |"
echo "+----------------------------------------------------------------------+"
echo ""
echo "Certificate of Completion:"
cat creative/05_certificate.txt

echo ""
echo "Python Banner Test:"
python3 creative/06_python_banner.py
