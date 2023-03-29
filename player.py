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
        print(f"\n{self.player_name} ako CADI!!")
        return True   
  
        
    def play(self, played_deck, index, card_symbol=None, wildcard=False):
        card = self.player_deck[index]

        if wildcard:
            return False
        
        elif card_symbol is not None and card.card_symbol != card_symbol:
            print(f"\n{card} cannot be played. The card symbol must be {card_symbol}.")
            return False
        
        if not (card.card_title == "Ace" or card.card_title == "Joker") and card.card_title == played_deck[-1].card_title or card.card_symbol == played_deck[-1].card_symbol:
            played_deck.append(card)
            self.player_deck.remove(card)   
            return True
        else:
            print(f"\n{card} is not playable.")

            return False

        

    def display_cards(self):
        for i, card in enumerate(self.player_deck):
            print(f"[{i+1}] {card}")
    
    def check_win(self):
        return len(self.player_deck) == 0
       