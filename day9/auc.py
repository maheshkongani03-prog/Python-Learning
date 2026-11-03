def highest(bidding_dic):
    max=0
    winner=''
    for bidder in bidding_dic:
        bid_amount=bidding_dic[bidder]
        if bid_amount>max:
            max=bid_amount
            winner=bidder
    print(f"The winner is {winner} with bidding amount of {max}")

bids={}
continuee=True
while continuee:
    names=input("What is the bidder name:")
    amnt=int(input("What is the bidding amount:"))
    bids[names]=amnt
    should_continue=input("Is there any bidders? y for yes otherwise n:").lower()
    if should_continue=='y':
        print("\n"*20)
    elif should_continue=='n':
        continuee=False
        highest(bids)
    else:
        print("Type correctly!!!")
        should_continue=input("Is there any bidders? y for yes otherwise n:").lower()
