# Day 60 - Auto Form Filler Demo

## What I Learned

- How Selenium automates browser actions
- Why selectors matter in form automation
- Why dry-run thinking is important before live automation

## Features

- Prepares example form data
- Shows a demo path if Selenium is missing
- Keeps the script safe and non-destructive by default

## How to Run

```bash
python main.py
```

## Example Output

```text
Welcome to Auto Form Filler Demo!
Selenium is not installed. Demo mode only.
Would fill name = Nayem
Would fill email = nayem@example.com
Would fill message = This is a demo form submission.
```

## Mistakes I Fixed

- Avoided running live automation without setup
- Kept field data separate from browser logic

## Future Improvement

- Add a local demo form page for testing
