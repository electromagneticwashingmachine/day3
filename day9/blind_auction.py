# from replit import clear
#HINT: You can call clear() to clear the output in the console.
from blind_art import logo
import os

print(logo) 

bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    # bidding_record = {"angela": 123, "James": 321}
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"The winner is {winner} with a bid of ${highest_bid}")

while not bidding_finished:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'. \n")
    if should_continue == "no":
        bidding_finished = True
        find_highest_bidder(bids)
        
    elif should_continue == "yes":
        os.system('cls' if os.name == 'nt' else 'clear')



























''' this is my version
bidders = {}
auction = True
while auction is True:
    new_bidders =  {}
    bidders_name = input("What is your name?:  ")
    bid_value = int(input("What is your bid?: $"))
    new_bidders[bidders_name] = bid_value
    bidders.update(new_bidders)
    bid_again = input("Are there any other bidder? type 'yes' or 'no'. \n")
    if bid_again == "yes":
        auction = True
       
    else:
        auction = False
        highest_bid = 0
        for key in bidders:
            value = bidders[key]
            if value > highest_bid:
                highest_bid = value
print(highest_bid)




print(bidders)

'''