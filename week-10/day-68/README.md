# Day 68 - Flashcard App GUI

## What I Learned

- How GUI polish improves usability
- Why validation and messageboxes matter
- How a flashcard interface changes displayed state

## Features

- Shows a random flashcard prompt
- Reveals the answer on demand
- Warns the user if no card is selected yet

## How to Run

```bash
python main.py
```

## Example Output

```text
Opens a flashcard GUI with next-card and show-answer controls.
```

## Mistakes I Fixed

- Validated that a card exists before showing the answer
- Kept the current card in one shared state variable

## Future Improvement

- Add score tracking
