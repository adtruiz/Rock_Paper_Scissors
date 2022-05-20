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

#Write your code below this line 👇

import random

game_images = [rock, paper, scissors]

youChoose = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))

if youChoose == 0:
    print(rock)
elif youChoose == 1:
    print(paper)
else:
    print(scissors)

computerChoice = random.randint(0, 2)

print(f"Computer Chose: \n")
print(game_images[computerChoice])


if youChoose >= 3 or youChoose < 0:
  print("You typed an invalid number, you lose!")
elif youChoose == 0 and computerChoice == 2:
  print("You win!")
elif computerChoice == 0 and youChoose == 2:
  print("You lose")
elif computerChoice > youChoose:
  print("You lose")
elif youChoose > computerChoice:
  print("You win!")
elif computerChoice == youChoose:
  print("It's a draw")
