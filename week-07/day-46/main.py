class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def monthly_pay(self):
        return self.salary


class Manager(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus

    def monthly_pay(self):
        return self.salary + self.bonus


employee = Employee("Rahim", 30000)
manager = Manager("Jui", 50000, 10000)

print("Welcome to Employee and Manager Payroll Model!")
print(f"{employee.name}: {employee.monthly_pay():.2f}")
print(f"{manager.name}: {manager.monthly_pay():.2f}")
