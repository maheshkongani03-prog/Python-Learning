bids={}
def highest(bidding_dictonory):
    max=0
    winner=''
    for bidder in bidding_dictonory:
        bid_amount=bidding_dictonory[bidder]
        if max<bid_amount:
            max=bid_amount
            winner=bidder
    print(f"The winner is {winner} with a bidding amount {max}")
continue_bidding=True
while continue_bidding:
    names=input("What is your Name:")
    price=int(input("What is your  bid:"))
    bids[names]=price
    should_continue=input("if there any bidders? type 'y' if yes otherwise 'n':\n")
    if should_continue=='y':
        print("\n"*20)
    elif should_continue=='n':
        highest(bids)
        continue_bidding=False





    
