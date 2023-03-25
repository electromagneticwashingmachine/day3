dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
# dimensions[0] = 250 cannot change a tuple.
# for loop tuple
print("Original dimensions: ")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimensions: ")
for dimension in dimensions:
    print(dimension)

five_foods = ('bread', 'omelette', 'rice', 'fish fry', 'soup')
#five_foods[1] = 'salad'
print("\nWe serve the following:")
for five_food in five_foods:
    print(five_food.title())

five_foods = ('spaghetti', 'pizza', 'rice', 'fish fry', 'soup')
print("\nWe NOW serve the following:")
for five_food in five_foods:
    print(five_food.title())
