print("Welcome to Treasure Island!")
print("Your mission is to find the treasure.")

first_choice = input("Left or Right? ").lower()

if first_choice == "left":
    second_choice = input("Swim or Wait? ").lower()
    if second_choice == "wait":
        third_choice = input("Which door? Red, Blue, or Yellow? ").lower()
        if third_choice == "yellow":
            print("You found the treasure! You win!")
        elif third_choice == "red":
            print("Burned by fire. Game over.")
        elif third_choice == "blue":
            print("Eaten by beasts. Game over.")
        else:
            print("Wrong door. Game over.")
    else:
        print("Attacked by trout. Game over.")
else:
    print("You fell into a hole. Game over.")
