# Writing a Game:

# 1. Write a game that is Composed of cards in different color.
#    A player then can guess that if the color of a card is the same of the revealed card? Or pass the turn.
#    If passed, he will get the cards.

import random
colors = ["red", "green", "yellow", "blue", "black"]
number_of_each_color = 4


def get_deck(number_of_each_color, colors):
    deck = [i for _ in range(number_of_each_color) for i in colors]
    random.shuffle(deck)
    return deck


def game_logic(deck, score, first_card):
    if not first_card:
        first_card = deck.pop(0)
    second_card = deck.pop(0)
    flag = True
    print("-" * 30)
    print("first card:", first_card)
    user_input = input("1. hold card\n2. pass card\n(1 or 2)\n")

    if user_input == "1":
        check_hold_card(first_card, second_card, score)
    else:
        flag = False
        print("second card:", second_card)

    if flag:
        return score, None
    else:
        return score, first_card


def check_hold_card(first_card, second_card, score):
    if second_card == first_card:
        score += 1
        print("That's Right.")
    else:
        print("second card:", second_card)
        print("You guessed wrong.")


def print_start_game():
    print("Hello!\n\nThis is a color game.\n"
          "A player then can guess that if the color of a card is\n"
          "the same of the revealed card? Or pass the turn.\n"
          "If passed, he will get the cards.\n")


def run_game_loop(deck):
    score = 0
    first_card = None
    while deck:
        score, first_card = game_logic(deck, score, first_card)
    return score


def print_end_game(score):
    print(f"your score is {score}")
    print("Game is finished BYE!")


# 1. start the game (Greeting,...)
print_start_game()
# 2. Initialize data(Create deck, shuffle)
decks = get_deck(number_of_each_color, colors)
# 3. Run game Loop
user_score = run_game_loop(decks)
# 4. Ending(Show score, ...)
print_end_game(user_score)
