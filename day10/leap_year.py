print("Welcome to Leap year or not?")
# year = int(input("Which year do you want to check? "))
def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(year) and month == 2:
        return 29
    return month_days[month - 1]


# Do not change the code below
year = int(input("Enter a year: "))
month = int(input("Enter a mont: "))
days = days_in_month(year, month)
print(days)