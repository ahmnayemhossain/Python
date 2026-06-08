# Day 45 - Quiz App CLI

## What I Learned

- How one class can contain objects from another class
- How composition keeps data organized
- How a quiz flow can be modeled with objects

## Features

- Stores questions as objects
- Runs the quiz through a `Quiz` class
- Tracks the final score

## How to Run

```bash
python main.py
```

## Example Output

```text
Welcome to Quiz App CLI!
Capital of Bangladesh? Dhaka
2 + 2 = ? 4
Python is a programming language? yes/no yes
Final score: 3/3
```

## Mistakes I Fixed

- Kept each question inside its own object
- Stored the score inside the quiz object

## Future Improvement

- Show correct answers after wrong attempts
