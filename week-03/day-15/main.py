import random

print("Welcome to the Number Guessing Game!")

secret_number = random.randint(1, 20)
attempts_left = 5

while attempts_left > 0:
    guess = int(input(f"Guess a number between 1 and 20 ({attempts_left} attempts left): "))

    if guess == secret_number:
        print("Correct! You guessed the number.")
        break
    elif guess < secret_number:
        print("Too low.")
    else:
        print("Too high.")

    attempts_left -= 1

if attempts_left == 0 and guess != secret_number:
    print(f"Game over. The number was {secret_number}.")
