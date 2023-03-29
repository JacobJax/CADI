from art import text2art
import random
from card import Card
from player import Player
from card import SpecialCard

def create_deck():
    # create an empty deck array
    deck = []

    # create instances of all cards and add them to the deck
    for card_title in ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]:
        for card_symbol in ["Spades", "Hearts", "Diamonds", "Clubs"]:
            if card_title in ["Ace"] and card_symbol in ["Spades"]:
                special_power = "TITLE_AND_SYMBOL"
                card = SpecialCard((card_title, card_symbol), special_power)
            elif card_title in ["Ace"]:
                special_power = "SYMBOL"
                card = SpecialCard((card_title, card_symbol), special_power)
            elif card_title in ["2", "3"]:
                special_power = f"DRAW_{int(card_title)}_CARDS"
                card = SpecialCard((card_title, card_symbol), special_power)
            elif card_title in ["8", "Queen"]:
                special_power = "QUESTION"
                card = SpecialCard((card_title, card_symbol), special_power)
            elif card_title in ["Jack"]:
                special_power = "JUMP"
                card = SpecialCard((card_title, card_symbol), special_power)
            elif card_title in ["King"]:
                special_power = "KICKBACK"
                card = SpecialCard((card_title, card_symbol), special_power)
            else:
                card = Card((card_title, card_symbol))
            
            deck.append(card)

    # add two Joker cards to the deck
    joker_1 = SpecialCard(("Joker", "Black"), "DRAW_5_CARDS")
    joker_2 = SpecialCard(("Joker", "Red"), "DRAW_5_CARDS")
    deck.append(joker_1)
    deck.append(joker_2)

    # return the complete deck
    return deck

def print_deck(deck):
    print("\n")
    for card in deck:
        print(card)
    print("\n")

def shuffle_deck(deck):
    shuffled_deck = deck[:]
    random.shuffle(shuffled_deck)
    return shuffled_deck

def distribute_cards(num_players, deck, number_of_cards):
    if num_players * number_of_cards > len(deck):
        raise ValueError("Not enough cards in the deck to distribute to all players")
    
    hands = [[] for i in range(num_players)]  # create an empty hand for each player
    
    for i in range(number_of_cards):  # deal `number_of_cards` cards to each player
        for j in range(num_players):
            hands[j].append(deck.pop(0))  # remove the top card from the deck and add it to the player's hand
    
    return hands, deck


def distribute_hands_to_players(players, hands):
    if len(players) != len(hands):
        raise ValueError("Number of players and number of hands don't match")

    for i in range(len(players)):
        for card in hands[i]:
            player = players[i]
            player.add_card(card)

def deal_cards(player, deck, num_cards):
    if len(deck) >= num_cards:
        cards = deck[:num_cards]
        del deck[:num_cards]
        for card in cards:
            player.add_card(card)
    else:
        print("Not enough cards in deck!")
    return deck


def generate_players():
    while True:
        try:
            number_of_players = int(input("How many players are playing (AT LEAST 2): "))
            if number_of_players >= 2:
                break
            else:
                print("Please enter a valid integer greater than or equal to 2.")
        except ValueError:
            print("Please enter a valid integer greater than or equal to 2.")

    players = []
    for i in range(number_of_players):
        name = input(f"Enter the name of player {i+1}: ")
        player = Player(name)
        players.append(player)

    return players

def generate_cards(players, deck):
    print("\n[A] Classic [B] Four card\n")
    while True:
        game_type = input("Enter the type of game to play: ")
        if game_type.lower() == "a":
            hands, deck = distribute_cards(len(players), deck, 3)
            distribute_hands_to_players(players, hands)
            break
        elif game_type.lower() == "b":
            hands, deck = distribute_cards(len(players), deck, 4)
            distribute_hands_to_players(players, hands)
            break
        else:
            print("Invalid input. Please try again.\n")
    
    return deck

def play_card(player, p_deck, g_deck, req_symbol):
    print(f"\nPlayer {player.player_name}'s deck:")
    player.display_cards()

    top_card = p_deck[-1]
    while True:
        try:
            index = int(input("Enter the index of the card you want to play (starting from 1): ")) - 1
            if 0 <= index < len(player.player_deck):
                break
            else:
                print("Please enter a valid index.")
        except ValueError:
            print("Please enter a valid integer index.")

    # SORRY FUTURE ME!!
    # ----CODE CHAFU Starts Here-----#

    if top_card.is_special:
        if top_card.special_power == "TITLE_AND_SYMBOL":
            if not player.play(p_deck, index, wildcard = True):
                g_deck = deal_cards(player, g_deck, 1)
                
        elif top_card.special_power == "SYMBOL":
            if not player.play(p_deck, index, card_symbol = req_symbol):
                g_deck = deal_cards(player, g_deck, 1)

    else:
        if not player.play(p_deck, index, card_symbol = req_symbol):
            g_deck = deal_cards(player, g_deck, 1)

    # ----CODE CHAFU Ends Here-----#

    return p_deck, g_deck


def set_required_card_symbol():

    standard_symbols = ["Spades", "Hearts", "Diamonds", "Clubs"]

    while True:
        try:
            required_symbol = input("\nWhat symbol do you want to play: ")
            if required_symbol in standard_symbols:
                break
            else:
                print("Please enter a valid symbol.")
        except ValueError:
            print("Please enter a valid symbol")

    return required_symbol

def set_required_card_title_and_symbol():
    stadard_titles = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

    required_symbol = set_required_card_symbol()

    while True:
        try:
            required_title = input("\nWhat card title do you want to play: ")
            if required_title in stadard_titles:
                break
            else:
                print("Please enter a valid card title.")
        except ValueError:
            print("Please enter a valid card title")

    return f"{required_title} of {required_symbol}"

def get_first_non_special_card(deck):
    non_special_card = next((card for card in deck if not card.is_special), None)
    if non_special_card:
        deck.remove(non_special_card)
    return non_special_card

def draw_title(title):
    cadi_art = text2art(title, font='block')
    print(cadi_art)


# ------------- #
#   GAME LOOP   #
# --------------#

# ATLEAST WE GOT A NICE TITLE
draw_title("QAD1")

# create a deck and shuffle it
deck = create_deck()
shuffled_deck = shuffle_deck(deck)

# generate players and 
players = generate_players()
game_deck = generate_cards(players, shuffled_deck)

# initialize GAME Variables
required_symbol = None
is_game = None
played_deck = []

play_index = 1

# Add Starting card
starting_card = get_first_non_special_card(game_deck)
played_deck.append(starting_card)

# get top card
top_card = played_deck[-1]

# Initialize game state
current_player_index = 0
reverse_turns = False

# Game loop
while True:
    current_player = players[current_player_index]

    print("\n$==================================================================================$")
    print(f"\nIt's {current_player.player_name}'s turn.")

    # Display the top card on the played deck
    # display_text = f""
    print(f"\nTop card on the Playing Deck is: {top_card}.\nThe Card To Be Played should have a {top_card.card_title} and / or {top_card.card_symbol}")

    # show player's cards and tell them to choose
    played_deck, game_deck = play_card(current_player, played_deck, game_deck, required_symbol)
    
    # Move to the next player
    if not reverse_turns:
        current_player_index = (current_player_index + play_index) % len(players)
    else:
        current_player_index = (current_player_index - play_index) % len(players)
    
    # check if player is Game
    if current_player.check_game():
        is_game = current_player

    # Check if player has won
    if current_player.check_win() and is_game == current_player:
        print(f"\n{current_player.player_name} has won the game!")
        break

    # Check if the direction of turns should be reversed
    if top_card.is_special and top_card.special_power == "KICKBACK":
        reverse_turns = not reverse_turns
        played_deck.pop(-1)

    # Check if the next player should be skipped
    elif top_card.is_special and top_card.special_power == "JUMP":
        play_index += 1
        played_deck.pop(-1)

    # Check if the next player should play a specific symbol
    elif top_card.is_special and top_card.special_power == "SYMBOL":
        required_card = set_required_card_symbol()
        played_deck, game_deck = play_card(current_player, played_deck, game_deck, required_symbol)
        current_player_index = (current_player_index + play_index) % len(players)
        played_deck.pop(-1)

    # Check if the next player should play a specifi card
    elif top_card.is_special and top_card.special_power == "TITLE_AND_SYMBOL":
        required_card = set_required_card_title_and_symbol()
        played_deck, game_deck = play_card(current_player, played_deck, game_deck, required_symbol)
        current_player_index = (current_player_index + play_index) % len(players)
        played_deck.pop(-1)

    # Check if the next player should draw 2 cards
    elif top_card.is_special and top_card.special_power == "DRAW_2_CARDS":
        game_deck = deal_cards(current_player, game_deck, 2)
        current_player_index = (current_player_index + play_index) % len(players)
        played_deck.pop(-1)

    # Check if the next player should draw 3 cards
    elif top_card.is_special and top_card.special_power == "DRAW_3_CARDS":
        game_deck = deal_cards(current_player, game_deck, 3)
        current_player_index = (current_player_index + play_index) % len(players)
        played_deck.pop(-1)

    # Check if the next player should draw 5 cards
    elif top_card.is_special and top_card.special_power == "DRAW_5_CARDS":
        game_deck = deal_cards(current_player, game_deck, 5)
        current_player_index = (current_player_index + play_index) % len(players)
        played_deck.pop(-1)

    # Check if the PLayer played a question
    elif top_card.is_special and top_card.special_power == "QUESTION":
        if top_card.get_card_symbol in current_player.player_deck:
            played_deck, game_deck = play_card(players[current_player_index], played_deck, game_deck, required_symbol)
        else:
            game_deck = deal_cards(current_player, game_deck, 1) 

        current_player_index = (current_player_index + play_index) % len(players)
        played_deck.pop(-1)

    # Check if the game has ended due to lack of playable cards
    if len(game_deck) == 0:
        print("The game has ended in a draw!")
        break