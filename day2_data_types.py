# print("Welcome"[2])
# data1 = "123"
# data2 = 45
# data3 = 2.5
# data4 = True
# print(type(data1))
# print(type(data2))
# print(type(data3))
# print(type(data4))

# num_char = len(input("What is your name?"))
# print("Your name has " + str(num_char) + " characters.")

# two_digit_number = input("Type a two digit number: ")
# digit1 = int(two_digit_number[0])
# print(type(digit1))
# digit2 = int(two_digit_number[1])
# print(type(digit2))
# # add = int(digit1) + int(digit2)

# add = sum([digit1, digit2])
# print(type(add))
# print(add)

# print(3 * 3 + 3 / 3 - 3)
# print(3 * ((3 + (3 / 3)) - 3))
# print(3 * (3 + 3) / 3 - 3)

# height = input("Enter your height in meters: ")
# weight = input("Enter your weight in kilo: ")

# bmi = float(weight) / (float(height) ** 2)
# print(type(bmi))
# print(round(bmi, 2))

print("Welcome to Tip Calculator.")
total_bill = float(input("What is your total bill? $"))
percentage = int(input("What percentage tip would you like to give? 10, 12, 15? "))
split_bill = int(input("How many people to split the bill? "))

tip_percentage = percentage / 100
bill_with_percentage = (total_bill * tip_percentage + total_bill) / split_bill
print(f"Each person should pay: ${bill_with_percentage:.2f}")



