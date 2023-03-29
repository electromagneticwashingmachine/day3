print('Welcome to "Who\'s gonna pay?\n')
name_string = input("Give me everybody's names, separated by comma(,).\n")
names = name_string.split(", ")

import random
random_index = random.randint(0, len(names) -1)
random_name = names[random_index]
print(f"The one that will pay for today is {random_name}")
