# === AutoKey Cipher ===

def encrypt(text, keyword):
    text = text.upper().replace(" ", "")
    keyword = keyword.upper()
    
    # Generate Key Stream: Keyword + Plaintext
    key_stream = keyword + text 
    # Truncate to match plaintext length
    key_stream = key_stream[:len(text)]
    
    cipher_text = ""
    for i in range(len(text)):
        p = ord(text[i]) - 65
        k = ord(key_stream[i]) - 65
        # Encryption: (P + K) mod 26
        c = (p + k) % 26
        cipher_text += chr(c + 65)
        
    return cipher_text, key_stream

def decrypt(cipher, keyword):
    cipher = cipher.upper()
    keyword = keyword.upper()
    
    # In AutoKey decryption, we reconstruct the key stream dynamically.
    # The plaintext character recovered at index i becomes the key for index i + len(keyword).
    
    full_plaintext = ""
    
    # Initialize keystream with the keyword
    keystream_list = list(keyword)
    
    for i in range(len(cipher)):
        # If we run out of the initial keyword, append the previously recovered plaintext char
        if i >= len(keystream_list):
            # Calculate which plaintext character acts as the key here
            idx_plaintext_char = i - len(keyword)
            keystream_list.append(full_plaintext[idx_plaintext_char])
            
        k = ord(keystream_list[i]) - 65
        c = ord(cipher[i]) - 65
        
        # Decryption: (C - K) mod 26
        p = (c - k) % 26
        char_p = chr(p + 65)
        full_plaintext += char_p
        
    return full_plaintext

def main():
    print("=== AutoKey Cipher Test ===")
    text = "ATTACKATDAWN"
    keyword = "Q" # Simple single char keyword example
    
    print(f"Plaintext: {text}")
    
    cipher, used_key = encrypt(text, keyword)
    print(f"KeyStream: {used_key}")
    print(f"Ciphertext:{cipher}")
    
    decrypted = decrypt(cipher, keyword)
    print(f"Decrypted: {decrypted}")

if __name__ == "__main__":
    main()