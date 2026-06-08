# Day 23 - Student Result Management CLI

## What I Learned

- How nested dictionaries store grouped data
- How lists can live inside dictionaries
- How to read and summarize nested values

## Features

- Keeps multiple students in one dictionary
- Stores each student's marks in a list
- Prints the average score for each student

## How to Run

```bash
python main.py
```

## Example Output

```text
Welcome to Student Result Management CLI!
Rahim: marks=[78, 82, 90], average=83.33
Karim: marks=[65, 70, 68], average=67.67
Jui: marks=[88, 92, 85], average=88.33
```

## Mistakes I Fixed

- Kept marks inside a nested structure for each student
- Calculated averages from the inner list correctly

## Future Improvement

- Add user input to create new student records
