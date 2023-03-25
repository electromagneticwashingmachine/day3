players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("This is a list without slicing. " + str(players))
print("This is a list with slicing. " + str(players[0:3]) + "\n")
print("If you omit the first index in a slice, \nPython automatically starts at \
the \nbeginning of the list! \nlike this " + str(players[:4]) + "\n")
print("Similarly if you want slice to\ninclude until the end of the list,\nyou\
 do like this.." + str(players[2:]) + "\n")
print("This prints the names of the last\nthree players and would continue to\
\nwork as the list of players changes size.\nLike this.. " + str(players[-3:]) + "\n")
print("\nHere are the first three players on my team: ")
for player in players[:3]:
    print(player.title())

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
print("\nMy favorite foods are: ")
print(my_foods)
print("\nMy friend's favorite foods are: ")
print(friend_foods)
my_foods.append('cannoli')
friend_foods.append('ice cream')
print("My favorite foods are: ")
print(my_foods)
print("\nMy friend's favorite foods are: ")
print(friend_foods)

print("My first three favorite food from my list are: " + str(my_foods[:3]))
my_foods.append('momo')
my_foods.append('salad')
my_foods.append('panipoori')
print("My new favorite foods are: " + str(my_foods))
print("Middle three foods are " + str(my_foods[2:5]))
print("The last three items are: " + str(my_foods[4:]))
friend_foods = my_foods[:]
friend_foods.append('spaghetti')
my_foods.append('aloo paratha')
print("My gaya-gaya friend's food are: " + str(friend_foods))
print("My fav foods now are: " + str(my_foods))

print("\nHere are the first three foods on my food list: ")
for my_food in my_foods[:3]:
    print(my_food.title())

print("\nHere are the last three foods my friend's food list: ")
for friend_food in friend_foods[5:]:
    print(friend_food.title())

