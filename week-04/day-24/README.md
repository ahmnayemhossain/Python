# Day 24 - Auction or Bidding App

## What I Learned

- How functions work with dictionary data
- How to scan dictionary values to find a winner
- How to keep bidding logic clean in a function

## Features

- Collects bidder names and amounts
- Stores bids in a dictionary
- Finds the highest bid and prints the winner

## How to Run

```bash
python main.py
```

## Example Output

```text
Welcome to the Auction or Bidding App!
Enter bidder name: Rahim
Enter bid amount: 500
Add another bidder? yes/no: yes
Enter bidder name: Jui
Enter bid amount: 650
Add another bidder? yes/no: no
Winner: Jui with bid 650
```

## Mistakes I Fixed

- Moved winner selection into a separate function
- Compared each bid amount against the current highest bid

## Future Improvement

- Add hidden bidding rounds
