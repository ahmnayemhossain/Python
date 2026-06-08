# Day 33 - Password Vault JSON V1

## What I Learned

- How JSON stores structured data
- How to save and load Python dictionaries with `json`
- How update flow works in a simple vault app

## Features

- Saves account passwords in a JSON file
- Shows all saved accounts
- Searches one account by name

## How to Run

```bash
python main.py
```

## Example Output

```text
Welcome to Password Vault JSON V1!

1. Add password
2. View all accounts
3. Search account
4. Exit
Choose an option: 1
Enter account name: github
Enter password: secret123
Password saved.
```

## Mistakes I Fixed

- Loaded existing JSON before overwriting it
- Stored vault data in a dictionary for quick lookup

## Future Improvement

- Hide passwords while entering input
