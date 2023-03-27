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
    joker_1 = SpecialCard(("Joker", "Black"), "Wildcard")
    joker_2 = SpecialCard(("Joker", "Red"), "Wildcard")
    deck.append(joker_1)
    deck.append(joker_2)

    # return the complete deck
    return deck

def print_deck(deck):
    for card in deck:
        print(card)

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
    
    return hands


def distribute_hands_to_players(players, hands):
    if len(players) != len(hands):
        raise ValueError("Number of players and number of hands don't match")

    for i in range(len(players)):
        for card in hands[i]:
            player = players[i]
            player.add_card(card)

def deal_card(player, deck):
    if len(deck) > 0:
        card = deck.pop(0)
        player.add_card(card)
    else:
        print("No more cards in deck!")


# create a deck and shuffle it
deck = create_deck()
shuffled_deck = shuffle_deck(deck)

# create some players
player1 = Player("Alice")
player2 = Player("Bob")
player3 = Player("Charlie")
players = [player1, player2, player3]

# deal some cards to the players
hands = distribute_cards(len(players), shuffled_deck, 4)
distribute_hands_to_players(players, hands)

# print the players' decks
for player in players:
    print(f"{player.display_cards()}\n")
