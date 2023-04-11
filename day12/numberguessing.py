from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def check_answer(guess, answer, turns):
    """checks answers against guess. Returns the number of turns remaining."""
    if guess > answer:
        print("Too High.")
        return turns - 1
    elif guess < answer:
        print("Too Low")
        return turns - 1
    else:
        print(f"You got it! The number was {answer}")

def set_difficulty():
    level = input("Choose difficulty. Type 'easy' or 'hard':  ").lower()
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    answer = randint(1, 100 )
    print(answer)
    turns = set_difficulty()
    

    guess = 0

    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess:  "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print(f"The right answer is {answer}, you Lose.")
            return
game()


# def compute_guess(guess):
#     if guess > random_number:
#         return "Too High."
#     elif guess < random_number:
#         return "Too Low."
#     else:
#         print(f"You got it! The number is {random_number}")

# if difficulty == "easy":
#     print(f"You have {hard_attempts} attempts remaining to guess the number.")
#     guess = int(input("Make a guess:  "))
# else:
#     print(f"You have {easy_attempts} attempts remaining to guess the number.")
#     guess = int(input("Make a guess:  "))

# print(guess)
# print(random_number)