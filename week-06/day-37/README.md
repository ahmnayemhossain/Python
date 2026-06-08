# Day 37 - Form Validator CLI

## What I Learned

- How custom exceptions improve validation
- How to raise meaningful errors
- How validation rules keep input safer

## Features

- Validates name length
- Validates email format
- Validates minimum age requirement

## How to Run

```bash
python main.py
```

## Example Output

```text
Welcome to Form Validator CLI!
Enter name: Nayem
Enter email: nayem@example.com
Enter age: 25
Valid form submitted for Nayem, nayem@example.com, age 25.
```

## Mistakes I Fixed

- Raised custom validation errors with clear messages
- Caught numeric conversion separately for age input

## Future Improvement

- Add password validation rules
