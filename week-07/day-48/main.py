class Drink:
    def __init__(self, name, water, milk, coffee):
        self.name = name
        self.water = water
        self.milk = milk
        self.coffee = coffee


class CoffeeMachine:
    def __init__(self, water, milk, coffee):
        self.water = water
        self.milk = milk
        self.coffee = coffee

    def can_make(self, drink):
        return (
            self.water >= drink.water
            and self.milk >= drink.milk
            and self.coffee >= drink.coffee
        )

    def make_drink(self, drink):
        if not self.can_make(drink):
            return "Not enough resources."
        self.water -= drink.water
        self.milk -= drink.milk
        self.coffee -= drink.coffee
        return f"{drink.name} served."


latte = Drink("Latte", 200, 150, 24)
machine = CoffeeMachine(400, 300, 100)

print("Week 07 Exam - OOP Coffee Machine App")
print(machine.make_drink(latte))
print(f"Water left: {machine.water}")
