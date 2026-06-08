# Day 38 - Number Filter Tool

## What I Learned

- How list comprehensions build new lists
- How conditions work inside comprehensions
- How concise filtering can stay readable

## Features

- Converts text input into a number list
- Filters even and positive numbers
- Prints numbers greater than 10 separately

## How to Run

```bash
python main.py
```

## Example Output

```text
Welcome to Number Filter Tool!
Enter numbers separated by spaces: 4 -2 15 9 20
Even numbers: [4, -2, 20]
Positive numbers: [4, 15, 9, 20]
Numbers greater than 10: [15, 20]
```

## Mistakes I Fixed

- Converted the input strings to integers before filtering
- Used separate comprehensions to keep each result clear

## Future Improvement

- Add custom filter options
