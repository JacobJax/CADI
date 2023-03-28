import re
from card import Card, SpecialCard

class Player:
    def __init__(self, player_name):
        self.player_name = player_name
        self.player_deck = []

    def add_card(self, card):
        self.player_deck.append(card)

    def remove_card(self, index):
        del self.player_deck[index]

    def check_game(self):
        for card in self.player_deck:
            if card.is_special:
                return False
        print(f"{self.player_name} ako CADI!!")
        return True   
    
    def play(self, played_deck, index):
        card = self.player_deck[index]
        if card.title == played_deck[-1].title or card.symbol == played_deck[-1].symbol:
            self.deck.remove(card)
            played_deck.append(card)
            print(card)
        else:
            print(f"{card} is not playable.")

    def display_cards(self):
        print(f"{self.player_name}'s cards:")
        for i, card in enumerate(self.player_deck):
            print(f"[{i+1}] {card}")

    
    def check_win(self):
        return len(self.player_deck) == 0
       