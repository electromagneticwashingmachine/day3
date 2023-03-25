print("Welcome to Leap year or not?")
year = int(input("Which year do you want to check? "))

if year % 4 == 0:
    if year % 100 == 0:
       if year % 400 == 0:
           print(f"The year {year} is a Leap Year!")
       else:
           print(f"The year {year} is a Not a Leap Year!")
    else:
        print(f"The Year {year} is a Leap Year!")

else:
    print(f"The year {year} is NOT a leap year.")