# Writing a Game:

# 1. Write a game that is Composed of cards in different color.
#    A player then can guess that if the color of a card is the same of the revealed card? Or pass the turn.
#    If passed, he will get the cards.

def game_logic(deck, score):
    return score

# definition of the functions
def is_game_ended(deck):
    return len(deck) == 0

def print_start_game():
    print("This is a color game, you can.")
    print("A player then can guess that if the color of a card is the same of the revealed card? Or pass the turn."
          "If passed, he will get the cards.")
    
def get_deck():
    # TODO: to be changed Later
    return ["Yellow", "Red", "Blue", "Red", "Blue", "Yellow"]

def run_game_loop(deck):
    score = 0
    while True:
        if is_game_ended(deck) == True:
            break
        score = game_logic(deck, score)
    return score

def print_end_game(score):
    print(f"your score is {score}")
    print("Game is finished BYE!")
#


# Piri => Structure the program.
# 1. start the game (Greeting,...)
print_start_game()
# 2. Initialize data(Create deck, shuffle)
deck = get_deck()
# 3. Run game Loop
score = run_game_loop(deck)
# 4. Ending(Show score, ...)
print_end_game(score)
