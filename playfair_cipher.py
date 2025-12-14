# === Playfair Cipher (Preprocessing & Matrix Generation) ===

def create_matrix(key):
    # Prepare key: Uppercase and treat J as I
    key = key.upper().replace("J", "I")
    matrix = []
    seen = set()
    
    # 1. Add key characters first (unique)
    for char in key:
        if char not in seen and char.isalpha():
            matrix.append(char)
            seen.add(char)
    
    # 2. Fill the rest with remaining alphabet (excluding J)
    for i in range(65, 91):
        char = chr(i)
        if char == "J": continue
        if char not in seen:
            matrix.append(char)
            seen.add(char)
            
    # Convert linear list to 5x5 grid (list of lists)
    grid = [matrix[i:i+5] for i in range(0, 25, 5)]
    return grid

def prepare_text(text):
    text = text.upper().replace("J", "I").replace(" ", "")
    processed_text = ""
    
    i = 0
    while i < len(text):
        a = text[i]
        b = ""
        
        if (i + 1) < len(text):
            b = text[i + 1]
        
        if a == b:
            # If letters are the same, insert filler 'X'
            processed_text += a + "X"
            i += 1
        elif b != "":
            # If letters are different, take the pair
            processed_text += a + b
            i += 2
        else:
            # Handle odd length at the end by adding 'X'
            processed_text += a + "X"
            i += 1
            
    return processed_text

def print_matrix(matrix):
    print("Key Matrix (5x5):")
    for row in matrix:
        print(" ".join(row))

def main():
    print("=== Playfair Cipher (Matrix & Prep) ===")
    
    key_input = "MONARCHY"
    text_input = "BALLOON"
    
    # 1. Create Matrix
    matrix = create_matrix(key_input)
    print_matrix(matrix)
    
    # 2. Process Text
    # BALLOON -> BALXLXOON (due to LL and OO) -> padded with X at end
    processed = prepare_text(text_input)
    
    # Split into pairs for display
    pairs = [processed[i:i+2] for i in range(0, len(processed), 2)]
    
    print(f"\nOriginal Text:  {text_input}")
    print(f"Processed Text: {processed}")
    print(f"Digraphs:       {pairs}")

if __name__ == "__main__":
    main()