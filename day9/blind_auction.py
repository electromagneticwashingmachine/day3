# from replit import clear
#HINT: You can call clear() to clear the output in the console.
from blind_art import logo
print(logo) 

bidders = {}
bidders_name = input("What is your name?:  ")
bid = int(input("What is your bid?: $"))
bid_again = input("Are there any other bidder? type 'yes' or 'no'. \n")
bidders[bidders_name] = bid


print(bidders)