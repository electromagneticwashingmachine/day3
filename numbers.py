for value in range(1,6):
    print(value)
print("The last number is " + str(value) + ".\n")

even_numbers = list(range(2,11,2))
print("This are the even numbers: " + str(even_numbers))

odd_numbers = list(range(1,12,2))
print("This are the odd numbers: " + str(odd_numbers) + "\n")

squares = []
for value in range(1,11):
#    square = value**2
    squares.append(value**2)
print(squares)
maximum = max(squares)
minimum = min(squares)
summary = sum(squares)
print("The maximum number on the list is " + str(maximum) + ", while the minimum is " + str(minimum) + ".")
print("If you add all this numbers, the total will be " + str(summary) + ".")
# This is "list comprehension" it will show same result, but in a shorter way to code.
squares = [value**2 for value in range(1,11)]
print("This is shorter way to code, but produces same result! " + str(squares))

counting_twenty = [value for value in range(1,21)]
print("I will count 1 to 20, see my output! " + str(counting_twenty))

counting_1million = [value for value in range(1,1000001)]
print(str(counting_1million) + "\n...this how you count 1 to a million!\n")

threes = [value*3 for value in range(3,31)]
print("Starting at number 3, we mulptiply it by 3 until we reach 30. This is the result! " + str(threes))

cubes = str([value**3 for value in range(1,10)])
print("This is when to cube! From 1 to 10... " + cubes)
