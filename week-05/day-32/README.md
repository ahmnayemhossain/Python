# Day 32 - Expense Tracker CSV

## What I Learned

- How to use Python's `csv` module
- How to write and read CSV rows
- How file-based expense data can be summarized

## Features

- Saves expenses by category
- Reads saved expenses from a CSV file
- Calculates the total expense amount

## How to Run

```bash
python main.py
```

## Example Output

```text
Welcome to Expense Tracker CSV!

1. Add expense
2. View expenses
3. Exit
Choose an option: 1
Enter category: Food
Enter amount: 250
Expense saved.
```

## Mistakes I Fixed

- Used `newline=""` while working with CSV files
- Converted string amounts back to floats for totals

## Future Improvement

- Add date support for each expense
