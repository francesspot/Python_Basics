import random
from art import logo

def guessing_game():
    print(logo)
    print("Welcome to Number Guessing Game!")
    print("I am thinking of a number between 1 and 100")
    mode = input("Choose a difficulty. Type 'easy' or 'hard': ")

    number = random.randint(1, 100)
    lives = 0

    if mode == "easy":
        lives = 10
    elif mode == "hard":
        lives = 5


    while lives > 0:
        print(f"You have {lives} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess == number:
            print("You guessed the number!")
            return
        elif guess > number:
            print("Too high!")
            lives -= 1
        else:
            print("Too low!")
            lives -= 1
    print("You've run out of guesses.")
    return

guessing_game()