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
