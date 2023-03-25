print("Welcome to the Rollercoaster!")
height = int(input("What is your height in cm? "))
ticket = 0

# Design a Rollercoaster app check if
# User are in within height limit (120cm)
# User must enter a age group for ticket price.
# User will choose if he wants to take a photo, which additional $3
if height >= 120:
    print(f"Your height is {height}cm, you can ride the Rollercoaster!") 
    age = int(input("What is your age? "))
    if age < 12:
        ticket = 5
        print(f"Your age is {age}. Ticket is $5.")
    elif age <= 18:
        ticket = 7
        print(f"Your age is {age}. Ticket is $7.")
    elif age >= 45 and age <= 55:
        print(f"Your age is {age}, you are Free to ride!")
    else:
        ticket = 12
        print(f"Your age is {age}. Ticket is $12.")
    
    wants_photo = input("Would you like to take a photo? Y or N: ").upper()
    if wants_photo == "Y":
        ticket += 3
        print(f"Your total bill is ${ticket}")

else:
    print("Sorry, you have to grow taller before you can ride.")