class CoffeeMachine:
    def __init__(self, water, milk, coffee):
        self.water = water
        self.milk = milk
        self.coffee = coffee

    def make_latte(self):
        if self.water >= 200 and self.milk >= 150 and self.coffee >= 24:
            self.water -= 200
            self.milk -= 150
            self.coffee -= 24
            return "Latte is ready!"
        return "Not enough resources."

    def status(self):
        return f"Water: {self.water}ml, Milk: {self.milk}ml, Coffee: {self.coffee}g"


machine = CoffeeMachine(500, 400, 100)

print("Welcome to Coffee Machine OOP V1!")
print(machine.status())
print(machine.make_latte())
print(machine.status())
