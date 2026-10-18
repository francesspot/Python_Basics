import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def has_blackjack(hand):
    if sum(hand) == 21:
        return True
    else:
        return False

def sum_score(hand):
    while sum(hand) > 21 and 11 in hand:
        hand[hand.index(11)] = 1
    return sum(hand)

def print_hands(hand1, hand2):
    print(f"User hand: {hand1} (Score: {sum_score(hand1)})")
    print(f"Computer hand: {hand2} (Score: {sum_score(hand2)})")

want_to_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n':")

deck_length = len(cards)

def blackjack():
    user_hand = []
    computer_hand = []
    for i in range(2):
        user_hand.append(random.choice(cards))
        computer_hand.append(random.choice(cards))

    user_score = sum_score(user_hand)
    computer_score = sum_score(computer_hand)

    if has_blackjack(computer_hand):
        print("You lose!")
        print_hands(user_hand, computer_hand)
    elif has_blackjack(user_hand):
        print("You win!")
        print_hands(user_hand, computer_hand)
    else:
        print(f"Computer first card is {computer_hand[0]}")
        print(f"Your current hand: {user_hand} (Score: {user_score})")

    while user_score < 21:
        another_card = input("Do you want to draw another card? Type 'y' or 'n':")
        if another_card == "y":
            user_hand.append(random.choice(cards))
            user_score = sum_score(user_hand)
            print(f"Your current hand: {user_hand} (Score: {user_score})")
        else:
            break

    if user_score > 21:
        print("You went over 21. You lose!")
    elif computer_score > 21:
        print("Computer went over 21. You win!")
    elif user_score > computer_score:
        print("You win!")
    elif user_score == computer_score:
        print("It's a draw!")
    else:
        print("You lose!")
    print_hands(user_hand, computer_hand)

    play_again = input("Do you want to play again? Type 'y' or 'n': ")
    if play_again == "y":
        print("\n " * 20)
        blackjack()

if want_to_play == 'y':
    blackjack()