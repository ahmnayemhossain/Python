# Day 31 - File Organizer Dry Run

## What I Learned

- How relative and absolute paths differ
- How `Path.resolve()` gives a full path
- How to inspect files without moving them

## Features

- Scans a target folder
- Reads file extensions
- Prints dry-run move suggestions only

## How to Run

```bash
python main.py
```

## Example Output

```text
Welcome to File Organizer Dry Run!
Enter a folder path or press Enter for current folder:
Scanning: C:\Users\USER\desktop\python
Would move README.md to folder md
```

## Mistakes I Fixed

- Resolved the target folder before scanning
- Avoided moving files because this is only a dry run

## Future Improvement

- Add real move support with confirmation
