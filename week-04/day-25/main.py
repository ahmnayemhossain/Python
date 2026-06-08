def fixed_average(numbers):
    print(f"DEBUG: received numbers = {numbers}")
    total = sum(numbers)
    count = len(numbers)
    print(f"DEBUG: total = {total}, count = {count}")
    return total / count


def fixed_discount(price, percent):
    print(f"DEBUG: price = {price}, percent = {percent}")
    discount = price * percent / 100
    return price - discount


print("Welcome to the Bug-Fix Challenge Pack!")

sample_numbers = [10, 20, 30, 40]
print(f"Average: {fixed_average(sample_numbers):.2f}")
print(f"Discounted price: {fixed_discount(1000, 15):.2f}")
