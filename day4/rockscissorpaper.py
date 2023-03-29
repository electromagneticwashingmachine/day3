import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

images = [rock, paper, scissors]

print("Welcome to Rock, Paper, Scissor Game!\n")

computer_choice = random.randint(0, 2)
player_choice = int(input("Type 0 for Rock, 1 for Paper or 2 for Scissors. \n"))
if player_choice < 0 or player_choice > 2:
    print("You enter a wrong number.")
else:
    print(images[player_choice])
    print(f"Computer chose: {computer_choice}")
    print(images[computer_choice])
    if player_choice == 0 and computer_choice == 2:
        print("You Win!")
    elif computer_choice == 0 and player_choice == 2:
        print("You Loose!")
    elif computer_choice > player_choice:
        print("You Loose!")
    elif player_choice > computer_choice:
        print("You Win!")
    elif player_choice == computer_choice:
        print("It's a tie!")

