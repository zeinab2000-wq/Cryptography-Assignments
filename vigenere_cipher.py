# === Vigenere Cipher ===

def generate_key(text, key):
    # Repeat the keyword until it matches the length of the text
    key = list(key)
    if len(text) == len(key):
        return key
    else:
        for i in range(len(text) - len(key)):
            key.append(key[i % len(key)])
    return "".join(key)

def encrypt(text, key):
    text = text.upper().replace(" ", "")
    key = generate_key(text, key.upper())
    cipher_text = []
    
    for i in range(len(text)):
        # Formula: (Pi + Ki) mod 26
        x = (ord(text[i]) + ord(key[i])) % 26
        x += 65
        cipher_text.append(chr(x))
    return "".join(cipher_text)

def decrypt(cipher_text, key):
    cipher_text = cipher_text.upper()
    key = generate_key(cipher_text, key.upper())
    orig_text = []
    
    for i in range(len(cipher_text)):
        # Formula: (Ci - Ki + 26) mod 26
        x = (ord(cipher_text[i]) - ord(key[i]) + 26) % 26
        x += 65
        orig_text.append(chr(x))
    return "".join(orig_text)

def main():
    print("=== Vigenere Cipher Test ===")
    text = "CRYPTO"
    keyword = "ABC"
    
    cipher = encrypt(text, keyword)
    print(f"Ciphertext: {cipher}")
    
    decrypted = decrypt(cipher, keyword)
    print(f"Decrypted:  {decrypted}")

if __name__ == "__main__":
    main()