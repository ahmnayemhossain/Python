class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
        return f"Product(name={self.name!r}, price={self.price!r})"

    def __str__(self):
        return f"{self.name} - {self.price:.2f} BDT"


class Cart:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def total(self):
        return sum(product.price for product in self.products)


cart = Cart()
cart.add_product(Product("Pen", 10))
cart.add_product(Product("Book", 80))

print("Welcome to Product Cart Model!")
for product in cart.products:
    print(product)
print(f"Cart total: {cart.total():.2f} BDT")
