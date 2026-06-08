def find_highest_bidder(bids):
    winner_name = ""
    highest_bid = 0

    for bidder_name, bid_amount in bids.items():
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner_name = bidder_name

    return winner_name, highest_bid


print("Welcome to the Auction or Bidding App!")

bids = {}

while True:
    bidder_name = input("Enter bidder name: ").strip()
    bid_amount = int(input("Enter bid amount: "))
    bids[bidder_name] = bid_amount

    more_bidders = input("Add another bidder? yes/no: ").lower()
    if more_bidders != "yes":
        break

winner_name, highest_bid = find_highest_bidder(bids)
print(f"Winner: {winner_name} with bid {highest_bid}")
