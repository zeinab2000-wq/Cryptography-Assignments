import sys

# === Additive Cipher (Caesar Cipher) ===

def encrypt(text, key):
    result = ""
    for char in text:
        if char.isalpha():
            # Formula: C = (P + K) mod 26
            # We normalize ASCII to 0-25 range
            shifted = (ord(char.upper()) - 65 + key) % 26
            result += chr(shifted + 65)
        else:
            result += char
    return result

def decrypt(text, key):
    # Decryption is encryption with the inverse key: P = (C - K) mod 26
    return encrypt(text, -key)

def brute_force(cipher_text):
    print("\n--- Starting Brute Force Attack ---")
    # Try all possible keys (1 to 25)
    for k in range(1, 26):
        decrypted_text = decrypt(cipher_text, k)
        print(f"Key {k:02}: {decrypted_text}")
    print("-----------------------------------")

def main():
    print("=== Additive Cipher Test ===")
    plaintext = "HELLO SECURITY"
    key = 3
    
    # 1. Encryption
    cipher = encrypt(plaintext, key)
    print(f"Plaintext:  {plaintext}")
    print(f"Ciphertext: {cipher}")
    
    # 2. Decryption
    decrypted = decrypt(cipher, key)
    print(f"Decrypted:  {decrypted}")
    
    # 3. Brute Force Attack
    brute_force(cipher)

if __name__ == "__main__":
    main()