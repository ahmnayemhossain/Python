# Day 40 - Birthday Reminder CLI

## What I Learned

- How the `datetime` module works with dates
- How to parse a date from text
- How to calculate days between dates

## Features

- Takes a name and birthday input
- Finds the next birthday date
- Prints how many days are left

## How to Run

```bash
python main.py
```

## Example Output

```text
Welcome to Birthday Reminder CLI!
Enter name: Jui
Enter birthday (YYYY-MM-DD): 2000-12-25
Jui's next birthday is in 200 day(s).
```

## Mistakes I Fixed

- Shifted the birthday to the next year if this year's date already passed
- Parsed the date with the correct ISO format

## Future Improvement

- Support multiple saved birthdays
