# Day 18 - Email Username and Domain Extractor

## What I Learned

- How string methods clean text
- How slicing extracts parts of a string
- How to locate special characters in text

## Features

- Takes an email address from the user
- Extracts the username before `@`
- Extracts the domain after `@`

## How to Run

```bash
python main.py
```

## Example Output

```text
Welcome to the Email Username and Domain Extractor!
Enter an email address: nayem@example.com
Username: nayem
Domain: example.com
```

## Mistakes I Fixed

- Trimmed extra spaces from the input
- Split the string at the correct `@` position

## Future Improvement

- Validate invalid email input
