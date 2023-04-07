# from replit import clear
#HINT: You can call clear() to clear the output in the console.
from blind_art import logo
print(logo) 

bidders = {}
auction = True
while auction is True:
    new_bidders =  {}
    bidders_name = input("What is your name?:  ")
    bid_value = int(input("What is your bid?: $"))
    new_bidders[bidders_name] = bid_value
    bidders.append(new_bidders)
    bid_again = input("Are there any other bidder? type 'yes' or 'no'. \n")
    if bid_again == "yes":
        auction = True
       
    else:
        auction = False



print(bidders)