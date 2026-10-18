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

game_images = [rock, paper, scissors]
player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

if player_choice >= 0 and player_choice <= 2:
    print(game_images[player_choice])

    computer_choice = random.randint(0, 2)

    print(f"Computer chose: \n {game_images[computer_choice]}")

    if computer_choice == player_choice:
        print("It's a draw!")
    elif computer_choice == 0 and player_choice == 2 or computer_choice == 1 and player_choice == 0:
        print("You lose!")
    else:
        print("You win!")
else :
    print("You typed an invalid number, you lose!")
