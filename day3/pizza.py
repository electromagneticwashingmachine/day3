print("Welcome to Python Pizza Deliveries!")
size = input("What size of pizza do you want? S, M or L: ").upper() 
add_pepperoni = input("Do you want pepperoni? Y or N: ").upper() 
extra_cheeze = input("Do you want extra cheese? Y or N: ").upper() 

bill = 0

if size == "L":
    bill += 25
elif size == "M":
    bill += 20
elif size == "S":
    bill += 15

if add_pepperoni == "Y":
    if size == "M" or size == "L":
        bill += 3
    else:
        bill += 2

if extra_cheeze == "Y":
    bill += 1

print(f"Your total bill is {bill}")
