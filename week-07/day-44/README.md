# Day 44 - Bank Account Simulator

## What I Learned

- How `__init__` prepares object data
- How attributes store balance and owner details
- How methods model deposit and withdrawal behavior

## Features

- Creates a bank account with an initial balance
- Supports deposits and withdrawals
- Prints the current account balance

## How to Run

```bash
python main.py
```

## Example Output

```text
Welcome to Bank Account Simulator!
Nayem's balance: 1000.00
Nayem's balance: 1500.00
1200
Nayem's balance: 1200.00
```

## Mistakes I Fixed

- Stored balance in the object instead of a global variable
- Checked insufficient balance before withdrawal

## Future Improvement

- Add transfer support
