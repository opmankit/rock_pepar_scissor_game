import random
rock  = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
images = [rock, paper, scissors]
user = int(input('What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n'))
if user >=3 or user < 0:
    print('invalid number , you lose!')
else:
    print(images[user])
    computer = random.randint(0,2)
    print('computer chose:')
    print(images[computer])
    if user == 0 and computer == 2:
        print('you win')
    elif computer == 0 and user == 2:
        print('you lose ')
    elif computer > user:
        print('you lose')
    elif user > computer:
        print('you win')
    elif computer ==user:
        print('draw')
