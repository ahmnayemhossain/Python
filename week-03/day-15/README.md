# Day 15 - Number Guessing Game

## What I Learned

- How `while` loops repeat until a condition changes
- How `break` stops a loop early
- How attempt counting keeps a game controlled

## Features

- Picks a random number from 1 to 20
- Gives multiple chances to the user
- Prints hints for high or low guesses

## How to Run

```bash
python main.py
```

## Example Output

```text
Welcome to the Number Guessing Game!
Guess a number between 1 and 20 (5 attempts left): 10
Too low.
Guess a number between 1 and 20 (4 attempts left): 15
Correct! You guessed the number.
```

## Mistakes I Fixed

- Reduced attempts after wrong guesses only
- Kept the winning check before the loop ends

## Future Improvement

- Add difficulty levels
