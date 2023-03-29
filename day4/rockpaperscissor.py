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

player = int(input("Type 0 for Rock, 1 for Paper or 2 for Scissors. \n"))

computer = random.randint(0, 2)
if player < 0 or player > 3:
    print("You enter wrong number!")
else:
    print(images[player])
    print(f"Computer chose... {computer}")
    print(images[computer])

if player == computer:
    print("It's a Tie!")

elif (player == 0 and computer == 2) or \
     (player == 2 and computer == 1) or \
     (player == 1 and computer == 0):
      print("You Win!")
elif (computer == 0 and player == 2) or \
     (computer == 2 and player == 1) or \
     (computer == 1 and player == 0):
      print("You Loose!")

else:
    print("No one Wins!")

