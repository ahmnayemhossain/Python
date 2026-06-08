ALPHABET = "abcdefghijklmnopqrstuvwxyz"


def shift_text(message, shift_amount):
    result = ""

    for character in message:
        if character.lower() in ALPHABET:
            current_index = ALPHABET.index(character.lower())
            new_index = (current_index + shift_amount) % len(ALPHABET)
            new_character = ALPHABET[new_index]
            result += new_character.upper() if character.isupper() else new_character
        else:
            result += character

    return result


print("Week 03 Exam - Caesar Cipher and Score Analyzer")

user_message = input("Enter a message: ")
shift_amount = int(input("Enter shift amount: "))
encrypted_message = shift_text(user_message, shift_amount)

scores_text = input("Enter scores separated by spaces: ")
scores = [int(score) for score in scores_text.split()]

print(f"Encrypted message: {encrypted_message}")
print(f"Lowest score: {min(scores)}")
print(f"Highest score: {max(scores)}")
print(f"Sorted scores: {sorted(scores)}")
