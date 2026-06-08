# Day 51 - Weather Checker CLI

## What I Learned

- How GET requests fetch API data
- How status codes affect response handling
- How JSON data can be read like nested dictionaries

## Features

- Accepts a city name
- Tries to fetch weather data from an API
- Falls back to demo data if needed

## How to Run

```bash
python main.py
```

## Example Output

```text
Welcome to Weather Checker CLI!
Enter city name: Dhaka
City: Dhaka
Temperature: 29 C
Condition: Partly cloudy (demo data)
```

## Mistakes I Fixed

- Added fallback data so the script still works offline
- Read nested JSON fields only after a successful response

## Future Improvement

- Add humidity and wind speed
