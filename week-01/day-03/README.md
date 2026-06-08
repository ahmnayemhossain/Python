# Day 03 - Tip Calculator

## What I Learned

- How to use `float()` and `int()` for type conversion
- How to format output with f-strings
- How to calculate and split a bill in Python

## Features

- Takes total bill input from the user
- Takes tip percentage and number of people
- Calculates per-person payment with two decimal places

## How to Run

```bash
python main.py
```

## Example Output

```text
Welcome to the Tip Calculator!
What was the total bill? 1500
How much tip would you like to give? 10, 12, or 15? 10
How many people to split the bill? 3
Each person should pay: 550.00
```

## Mistakes I Fixed

- Converted user input before doing arithmetic
- Formatted the final result to keep money output clean

## Future Improvement

- Add input validation for invalid numbers
