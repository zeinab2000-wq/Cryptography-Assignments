# === RC4 Algorithm: Complete Implementation (KSA, PRGA, Cipher) ===

def KSA(key):
    """
    Key Scheduling Algorithm (KSA)
    Initializes the state vector S based on the input key.
    """
    key_length = len(key)
    S = list(range(256))
    j = 0
    
    # KSA iteration: mixing the initial state
    for i in range(256):
        # j depends on S[i], the current key byte, and the previous j
        j = (j + S[i] + key[i % key_length]) % 256
        S[i], S[j] = S[j], S[i]  # Swap S[i] and S[j]
        
    return S

def PRGA(S, n_bytes):
    """
    Pseudo-Random Generation Algorithm (PRGA)
    Generates the keystream bytes using the initialized state vector S.
    """
    i = 0
    j = 0
    keystream = []
    
    # We must operate on a mutable copy of S
    S_copy = list(S)
    
    # PRGA iteration: generating the required number of keystream bytes
    for _ in range(n_bytes):
        i = (i + 1) % 256
        j = (j + S_copy[i]) % 256
        
        # Continuous swapping to maintain randomness
        S_copy[i], S_copy[j] = S_copy[j], S_copy[i]
        
        # Calculate the keystream byte (K)
        t = (S_copy[i] + S_copy[j]) % 256
        K = S_copy[t]
        keystream.append(K)
        
    return keystream

def rc4_cipher(data_bytes, keystream):
    """
    Performs the encryption or decryption using the XOR operation.
    In RC4, E = P XOR K and D = C XOR K.
    """
    output_bytes = []
    
    # XOR each data byte with the corresponding keystream byte
    for i in range(len(data_bytes)):
        result = data_bytes[i] ^ keystream[i]
        output_bytes.append(result)
        
    return output_bytes

def main():
    print("=== RC4 Full Encryption/Decryption Demonstration ===")
    
    # --- 1. Setup ---
    key_text = "SECRETKEY123"
    plaintext_text = "HELLO RC4 WORLD"
    
    # Convert text to lists of ASCII/byte values
    key = [ord(c) for c in key_text]
    plaintext_bytes = [ord(c) for c in plaintext_text]
    
    print(f"Key used: '{key_text}'")
    print(f"Plaintext: '{plaintext_text}'")
    
    # --- 2. Key Scheduling (KSA) ---
    S_initial = KSA(key)
    print("\n[Step 1: KSA Completed]")
    
    # --- 3. Keystream Generation (PRGA) ---
    # Generate a keystream exactly the length of the plaintext
    keystream = PRGA(S_initial, len(plaintext_bytes))
    print(f"[Step 2: PRGA] Generated Keystream (first 5 bytes): {keystream[:5]}...")
    
    # --- 4. Encryption ---
    ciphertext_bytes = rc4_cipher(plaintext_bytes, keystream)
    
    # Convert cipher bytes to a displayable format (often hard to read/unprintable characters)
    ciphertext_display = "".join([f"{b:02x}" for b in ciphertext_bytes])
    
    print("\n--- Encryption ---")
    print(f"Ciphertext (Hex): {ciphertext_display}")
    
    # --- 5. Decryption ---
    # The decryption uses the same keystream and the same XOR function
    decrypted_bytes = rc4_cipher(ciphertext_bytes, keystream)
    
    # Convert decrypted bytes back to readable text
    decrypted_text = "".join([chr(b) for b in decrypted_bytes])
    
    print("\n--- Decryption ---")
    print(f"Decrypted Text:   '{decrypted_text}'")
    
    # Verification
    if decrypted_text == plaintext_text:
        print("\nVerification: Success! Decrypted text matches original plaintext.")
    else:
        print("\nVerification: Failed!")

if __name__ == "__main__":
    main()