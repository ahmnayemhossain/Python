# Day 61 - File Download Organizer

## What I Learned

- Why automation safety checks matter
- How to sort files by extension
- Why duplicate handling prevents accidental overwrites

## Features

- Scans a chosen folder
- Moves files into extension-based subfolders
- Skips moves when a target file already exists

## How to Run

```bash
python main.py
```

## Example Output

```text
Welcome to File Download Organizer!
Enter download folder path or press Enter for current folder:
Scanning: C:\Users\USER\desktop\python
Moved sample.txt to txt/
```

## Mistakes I Fixed

- Checked for duplicate target files before moving
- Created destination folders only when needed

## Future Improvement

- Add dry-run mode
