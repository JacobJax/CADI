class Card:
    def __init__(self, card_tuple):
        self.card_title = card_tuple[0]
        self.card_symbol = card_tuple[1]

        self.is_special = False
        if self.card_title in ["Ace", "2", "3", "8", "Jack", "Queen", "King", "Joker"]:
            self.is_special = True

    def __str__(self):
        if self.is_special:
            return f"{self.card_title} of {self.card_symbol} ({self.special_power})"
        else:
            return f"{self.card_title} of {self.card_symbol}"
        
    def get_card_title(self):
        return self.card_title
    
    def get_card_symbol(self):
        return self.card_symbol


class SpecialCard(Card):
    def __init__(self, card_tuple, special_power):
        super().__init__(card_tuple)
        self.special_power = special_power
    
    def print_special_power(self):
        print("Special Power:", self.special_power)

    
