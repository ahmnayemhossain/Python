ALPHABET = "abcdefghijklmnopqrstuvwxyz"

print("Day 17 practice exercises")

print("\nExercise 1: Constant length")
print(len(ALPHABET))

print("\nExercise 2: Scope example")


def show_word():
    local_word = "python"
    print(local_word)


show_word()

print("\nExercise 3: Clean naming")
message_text = input("Enter a word: ")
print(message_text.upper())

print("\nExercise 4: Shift one letter")
letter = input("Enter one lowercase letter: ")
shifted_index = (ALPHABET.index(letter) + 2) % len(ALPHABET)
print(ALPHABET[shifted_index])

print("\nExercise 5: Function reuse")


def repeat_text(text_value):
    return text_value + text_value


print(repeat_text("Hi"))
