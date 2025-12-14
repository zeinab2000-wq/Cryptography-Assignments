import math

# === Multiplicative Cipher ===

def mod_inverse(a, m):
    # Calculate modular multiplicative inverse: (a * x) % m == 1
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def encrypt(text, key):
    # Condition: gcd(key, 26) must be 1 for a valid inverse to exist
    if math.gcd(key, 26) != 1:
        raise ValueError("Invalid Key: Key must be coprime to 26.")
        
    result = ""
    for char in text:
        if char.isalpha():
            # Formula: C = (P * K) mod 26
            val = ord(char.upper()) - 65
            encoded = (val * key) % 26
            result += chr(encoded + 65)
        else:
            result += char
    return result

def decrypt(text, key):
    inv_key = mod_inverse(key, 26)
    if inv_key is None:
        return "Cannot decrypt: Key has no modular inverse."
    
    result = ""
    for char in text:
        if char.isalpha():
            # Formula: P = (C * K^-1) mod 26
            val = ord(char.upper()) - 65
            decoded = (val * inv_key) % 26
            result += chr(decoded + 65)
        else:
            result += char
    return result

def brute_force(cipher_text):
    print("\n--- Multiplicative Cipher Brute Force ---")
    # Only try keys that are coprime to 26
    possible_keys = [k for k in range(1, 26) if math.gcd(k, 26) == 1]
    
    for k in possible_keys:
        try:
            decrypted = decrypt(cipher_text, k)
            print(f"Key {k:02}: {decrypted}")
        except:
            continue

def main():
    print("=== Multiplicative Cipher Test ===")
    plaintext = "HELLO"
    key = 7 # Valid key because gcd(7, 26) = 1
    
    try:
        cipher = encrypt(plaintext, key)
        print(f"Plaintext:  {plaintext}")
        print(f"Ciphertext: {cipher}")
        
        decrypted = decrypt(cipher, key)
        print(f"Decrypted:  {decrypted}")
        
        brute_force(cipher)
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()