# Game of Black Jack
import random


def deal_card():
    """Returns one random card from the deck"""
    cards_in_deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards_in_deck)


def calculate_score(cards_in_hand: list):
    """Returns sum of cards in hand. For BlackJack returns 0"""
    if sum(cards_in_hand) == 21 and len(cards_in_hand) == 2:
        return 0

    if 11 in cards_in_hand and sum(cards_in_hand) > 21:
        cards_in_hand.remove(11)
        cards_in_hand.append(1)

    return sum(cards_in_hand)


def compare(user_score: int, computer_score: int):
    """Takes score from user and computer, determines winner"""
    if user_score == computer_score:
        return "Draw!"
    elif computer_score == 0:
        return "Lose, oponent BlackJack"
    elif user_score == 0:
        return "Win! BlackJack"
    elif user_score > 21:
        return "You went over 21. You've lost."
    elif computer_score > 21:
        return "Opponent went over 21. You win!"
    elif user_score > computer_score:
        return "You have better cards. Winner!"
    else:
        return "Opponent has better score. You lose"


def game_blackjack():
    # initiate game
    user_cards = []
    computer_cards = []

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    # player turn
    while True:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        if user_score == 0 or computer_score == 0 or user_score >= 21:
            break
        else:
            print(f"your cards: {user_cards}, current score: {user_score}")
            print(f"computer cards: [{computer_cards[0]}, X]")
            user_another_draw = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if user_another_draw == 'y':
                user_cards.append(deal_card())
            else:
                break

    # computer turn
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand {user_cards}, final score: {user_score}")
    if user_score <= 21:
        print(f"Computer final hand {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))


if __name__ == "__main__":
    while True:
        if input("Fancy a BlackJack game?: 'y' to play, 'n' to exit: ").lower() != 'y':
            break
        print("\n" * 10)
        game_blackjack()
