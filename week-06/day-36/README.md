# Day 36 - Safe Calculator with Error Handling

## What I Learned

- How `try`, `except`, `else`, and `finally` work together
- How to catch bad input safely
- How to protect a calculator from common crashes

## Features

- Handles invalid numeric input
- Handles divide-by-zero errors
- Prints a final closing message every time

## How to Run

```bash
python main.py
```

## Example Output

```text
Welcome to Safe Calculator with Error Handling!
Enter first number: 12
Choose operation (+, -, *, /): /
Enter second number: 0
Error: Cannot divide by zero.
Calculator session finished.
```

## Mistakes I Fixed

- Caught divide-by-zero separately from other input problems
- Used `finally` so the session always ends cleanly

## Future Improvement

- Add repeated calculations in one session
