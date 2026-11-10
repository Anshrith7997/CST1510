alphabet = "abcdefghijklmnopqrstuvwxyz"

def encrypt(original_text, shift_amount):
    result = ""

    for letter in original_text:
        if letter.lower() in alphabet:
            position = alphabet.index(letter.lower())
            new_position = (position + shift_amount) % 26
            new_letter = alphabet[new_position]

            if letter.isupper():
                new_letter = new_letter.upper()

            result += new_letter
        else:
            result += letter

    return result