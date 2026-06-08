# Day 47 - Product Cart Model

## What I Learned

- How dunder methods improve object display
- Why `__repr__` and `__str__` serve different purposes
- How object models become easier to read with clean output

## Features

- Creates product objects with price data
- Adds products into a cart object
- Prints clean product lines and cart total

## How to Run

```bash
python main.py
```

## Example Output

```text
Welcome to Product Cart Model!
Pen - 10.00 BDT
Book - 80.00 BDT
Cart total: 90.00 BDT
```

## Mistakes I Fixed

- Added readable string output for products
- Calculated total with object attributes instead of raw lists

## Future Improvement

- Add quantity support
