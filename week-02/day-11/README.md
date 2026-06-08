# Day 11 - Shopping Cart CLI

## What I Learned

- How nested lists store grouped values
- How to loop through a cart summary
- How to accumulate a total price

## Features

- Adds item names and prices to a cart
- Prints a cart summary at the end
- Calculates the final total

## How to Run

```bash
python main.py
```

## Example Output

```text
Welcome to the Shopping Cart CLI!
Enter item name or 'done': Pen
Enter item price: 10
Enter item name or 'done': Book
Enter item price: 80
Enter item name or 'done': done

Cart Summary:
- Pen: 10.00
- Book: 80.00
Total: 90.00
```

## Mistakes I Fixed

- Kept name and price together with nested lists
- Used a running total inside the final loop

## Future Improvement

- Add quantity support
