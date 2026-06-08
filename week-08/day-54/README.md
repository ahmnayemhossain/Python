# Day 54 - Habit Tracker API Client

## What I Learned

- How POST, PUT, and DELETE differ
- How API payloads carry structured data
- Why network failures need a fallback plan

## Features

- Demonstrates create, update, and delete requests
- Uses `httpbin` when requests work
- Falls back to demo mode if needed

## How to Run

```bash
python main.py
```

## Example Output

```text
Welcome to Habit Tracker API Client!
Enter habit name: Reading
POST status: 200
PUT status: 200
DELETE status: 200
```

## Mistakes I Fixed

- Separated each HTTP method clearly
- Added a demo path for offline use

## Future Improvement

- Connect to a real habit tracking backend
