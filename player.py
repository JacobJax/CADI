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
    
    # def play(self, played_deck, index):
    #     card = self.player_deck[index]
    #     if not played_deck:
    #         self.player_deck.remove(card)
    #         played_deck.append(card)
    #         print(card)

    #         return True
    #     elif card.card_title == played_deck[-1].card_title or card.card_symbol == played_deck[-1].card_symbol:
    #         self.player_deck.remove(card)
    #         played_deck.append(card)
    #         print(card)

    #         return True
    #     else:
    #         print(f"\n{card} is not playable.")
            
    #         return False
        
    def play(self, played_deck, index, card_symbol=None, wildcard=False):
        card = self.player_deck[index]

        if wildcard:
            return False
        
        if card_symbol is not None and card.card_symbol != card_symbol:
            print(f"\n{card} cannot be played. The card symbol must be {card_symbol}.")
            return False
        
        if not played_deck:
            played_deck.append(card)
            self.player_deck.remove(card)

            print(card)
            self.display_cards()
            
            return True
        elif card.card_title == played_deck[-1].card_title or card.card_symbol == played_deck[-1].card_symbol:
            played_deck.append(card)
            self.player_deck.remove(card)

            print(card)
            self.display_cards()

            return True
        else:
            print(f"\n{card} is not playable.")
            
            return False

        

    def display_cards(self):
        for i, card in enumerate(self.player_deck):
            print(f"[{i+1}] {card}")
    
    def check_win(self):
        return len(self.player_deck) == 0
       