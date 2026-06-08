# Day 52 - Country Info Finder

## What I Learned

- How query-ready text is prepared for API calls
- How parameters shape a request
- How JSON country data can be extracted cleanly

## Features

- Accepts a country name from the user
- Tries to fetch country information from an API
- Falls back to demo data if needed

## How to Run

```bash
python main.py
```

## Example Output

```text
Welcome to Country Info Finder!
Enter country name: Bangladesh
Country: Bangladesh
Capital: Demo Capital
Population: 123456
Region: Demo Region
```

## Mistakes I Fixed

- Encoded user input before building the request URL
- Added safe fallback values for missing fields

## Future Improvement

- Show currency and language info too
