import random

print("Welcome to the Coin Toss and Dice Simulator!")

coin_result = random.choice(["Heads", "Tails"])
dice_result = random.randint(1, 6)

print(f"Coin toss result: {coin_result}")
print(f"Dice result: {dice_result}")
