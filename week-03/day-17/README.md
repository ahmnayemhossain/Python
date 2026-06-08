# Day 17 - Caesar Cipher V1

## What I Learned

- How constants make repeated values easier to manage
- How scope works inside and outside functions
- How clean variable names improve readability

## Features

- Shifts letters by a chosen amount
- Keeps non-letter characters unchanged
- Preserves uppercase letters

## How to Run

```bash
python main.py
```

## Example Output

```text
Welcome to Caesar Cipher V1!
Enter your message: Hello
Enter shift amount: 2
Encrypted message: Jgnnq
```

## Mistakes I Fixed

- Wrapped the shift index with modulo
- Preserved characters that are not letters

## Future Improvement

- Add decrypt mode
