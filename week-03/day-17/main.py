ALPHABET = "abcdefghijklmnopqrstuvwxyz"


def shift_text(message, shift_amount):
    result = ""

    for character in message:
        if character.lower() in ALPHABET:
            is_upper = character.isupper()
            current_index = ALPHABET.index(character.lower())
            new_index = (current_index + shift_amount) % len(ALPHABET)
            new_character = ALPHABET[new_index]
            result += new_character.upper() if is_upper else new_character
        else:
            result += character

    return result


print("Welcome to Caesar Cipher V1!")

user_message = input("Enter your message: ")
shift_amount = int(input("Enter shift amount: "))

encrypted_message = shift_text(user_message, shift_amount)

print(f"Encrypted message: {encrypted_message}")
