# Day 53 - Currency Converter with API

## What I Learned

- How environment variables protect secrets
- How `.env` files can supply configuration
- How API-key-based requests should fail safely

## Features

- Reads a currency amount and target conversion
- Uses an environment variable for the API key
- Falls back to demo rates when no key is set

## How to Run

```bash
python main.py
```

## Example Output

```text
Welcome to Currency Converter with API!
Enter base currency: USD
Enter target currency: BDT
Enter amount: 10
Using demo conversion data.
Converted amount: 1100.00 BDT
```

## Mistakes I Fixed

- Avoided hardcoding secrets in the script
- Added fallback conversion so the app still runs without a key

## Future Improvement

- Support more detailed exchange output
