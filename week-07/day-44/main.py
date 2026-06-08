class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient balance."
        self.balance -= amount
        return self.balance

    def show_balance(self):
        return f"{self.owner}'s balance: {self.balance:.2f}"


account = BankAccount("Nayem", 1000)

print("Welcome to Bank Account Simulator!")
print(account.show_balance())
account.deposit(500)
print(account.show_balance())
print(account.withdraw(300))
print(account.show_balance())
