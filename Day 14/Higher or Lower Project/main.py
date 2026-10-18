import random
from art import logo, vs
from game_data import data

def format_data(account):
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_description}, {account_country}"

def compare_followers(guess, account_A, account_B):
    if account_A > account_B:
        return guess == "a"
    else:
        return guess == "b"


def higher_or_lower():
    print(logo)

    game_continue = True
    score = 0
    account_B = random.choice(data)

    while game_continue:
        account_A = account_B
        account_B = random.choice(data)

        if account_A == account_B:
            account_B = random.choice(data)

        print(f"Compare A: {format_data(account_A)}")
        print(vs)
        print(f"Against B: {format_data(account_B)}")

        guess = input("Who has more followers? Type 'A' or 'B': ").lower()

        print("\n" * 20)
        print(logo)

        account_A_followers_count = account_A["follower_count"]
        account_B_followers_count = account_B["follower_count"]

        is_correct = compare_followers(guess, account_A_followers_count, account_B_followers_count)

        if is_correct:
            score += 1
            print(f"You are correct! Current score: {score}.")
        else:
            print(f"Sorry, that's wrong. Final score: {score}.")
            game_continue = False


higher_or_lower()