print("Welcome to Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

concat_name = name1.lower() + name2.lower()

l = concat_name.count("l")
o = concat_name.count("o")
v = concat_name.count("v")
e = concat_name.count("e")
love = l + o + v + e

t = concat_name.count("t")
r = concat_name.count("r")
u = concat_name.count("u")
e = concat_name.count("e")
true = t + r + u + e

string_score = str(true) + str(love)
integer_score = int(string_score)

if integer_score < 10 or integer_score > 90:
    print(f"Your score is {integer_score}, you go together like coke and mentos.")
elif integer_score >=40 and integer_score <= 50:
    print(f"Your score is {integer_score}, you are alright together.")    
else:
    print(f"Your score is {integer_score}.")

 