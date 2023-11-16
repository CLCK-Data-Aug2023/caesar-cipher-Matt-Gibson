def caesar_cipher(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            # Determine if the character is uppercase or lowercase
            is_upper = char.isupper()
            
            # Shift the character by the specified amount
            char_code = ord(char)
            shifted_code = (char_code - ord('A' if is_upper else 'a') + shift) % 26
            result += chr(shifted_code + ord('A' if is_upper else 'a'))
        else:
            # If the character is not a letter, keep it unchanged
            result += char

    return result

# Get input from the user
sentence = input("Enter a sentence: ")

# Apply Caesar cipher with a right shift of 5
encrypted_sentence = caesar_cipher(sentence, 5)

# Display the encrypted sentence
print("Encrypted sentence:", encrypted_sentence)
