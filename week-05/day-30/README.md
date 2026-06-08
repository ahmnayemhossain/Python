# Day 30 - Notes App Using Text File

## What I Learned

- How to open files for reading and writing
- How append mode keeps old content
- How file paths work with `Path`

## Features

- Saves notes into a text file
- Reads all saved notes
- Uses a simple menu flow

## How to Run

```bash
python main.py
```

## Example Output

```text
Welcome to Notes App Using Text File!

1. Add note
2. View notes
3. Exit
Choose an option: 1
Enter note text: Practice Python daily
Note saved.
```

## Mistakes I Fixed

- Opened the file in append mode when saving notes
- Checked if the file exists before reading

## Future Improvement

- Add note deletion support
