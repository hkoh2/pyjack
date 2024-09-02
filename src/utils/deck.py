from utils.card import Card
import random

class Deck:
    def __init__(self) -> None:
        self.suit = ["heart", "club", "spade", "diamond"]
        self.cards = []
        self.add_default_cards()

    def pop(self):
        if len(self.cards) <= 0:
            raise Exception('no more cards')
            
        return self.cards.pop()
        

    def add_default_cards(self):
        for suit in self.suit:
            self.cards.extend([Card(val, suit) for val in range(1, 14)])
        random.shuffle(self.cards)

    def show_remaining_cards(self):
        print("--- Cards remaining ---")
        for card in self.cards:
            card.to_string()
            card.val
        print("--- Cards remaining END---")