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
         print(self.player_deck[index])
         played_deck.add_card(self.player_deck[index])
         self.player_deck.remove(self.player_deck[index])

    def display_cards(self):
        print(f"{self.player_name}'s cards:")
        for card in self.player_deck:
            print(card)
       