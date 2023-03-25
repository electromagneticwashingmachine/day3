import random
print("Welcome to Flip Coin!")
coin = random.randint(0, 1)
if coin == 1:
    print("Your coin has head!")
else:
    print("Your coin has tail!")