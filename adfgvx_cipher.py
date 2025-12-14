import math

# === ADFGVX Cipher ===

# Constants
ADFGVX = "ADFGVX"
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

def create_polybius_square(key_sq):
    # Clean key and fill the matrix
    key_sq = key_sq.upper()
    seen = set()
    square = []
    
    # Add key characters
    for char in key_sq:
        if char in ALPHABET and char not in seen:
            square.append(char)
            seen.add(char)
            
    # Add remaining characters from ALPHABET (A-Z, 0-9)
    for char in ALPHABET:
        if char not in seen:
            square.append(char)
            seen.add(char)
            
    # Create 6x6 grid
    grid = [square[i:i+6] for i in range(0, 36, 6)]
    return grid

def encrypt(text, key_square_str, trans_key):
    # Phase 1: Substitution
    grid = create_polybius_square(key_square_str)
    
    # Create map for quick lookup
    char_map = {}
    for r in range(6):
        for c in range(6):
            char_map[grid[r][c]] = ADFGVX[r] + ADFGVX[c]
            
    text = text.upper().replace(" ", "")
    substituted_text = ""
    for char in text:
        if char in char_map:
            substituted_text += char_map[char]
            
    print(f"Substituted (Fractionation): {substituted_text}")
    
    # Phase 2: Transposition
    k_len = len(trans_key)
    # Pad text if not multiple of key length
    padding = (k_len - (len(substituted_text) % k_len)) % k_len
    substituted_text += "X" * padding 
    
    # Create Columns
    columns = {char: [] for char in trans_key}
    sorted_key = sorted(list(trans_key))
    
    # Fill columns
    col_idx = 0
    for char in substituted_text:
        key_char = trans_key[col_idx]
        columns[key_char].append(char)
        col_idx = (col_idx + 1) % k_len
        
    # Read columns based on alphabetical order of key
    cipher_text = ""
    for k_char in sorted_key:
        cipher_text += "".join(columns[k_char])
        
    return cipher_text

def main():
    print("=== ADFGVX Cipher Test ===")
    
    # Key for the 6x6 Polybius Square
    polybius_key = "NIGHT" 
    # Key for Columnar Transposition
    transposition_key = "CAR" 
    plaintext = "ATTACK10AM"
    
    print("Matrix 6x6 (First row):", create_polybius_square(polybius_key)[0])
    
    final_cipher = encrypt(plaintext, polybius_key, transposition_key)
    print(f"Final Ciphertext: {final_cipher}")

if __name__ == "__main__":
    main()