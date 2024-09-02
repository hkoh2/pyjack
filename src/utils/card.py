

class Card:

    card_value_visual = {
        1: 'A',
        11: 'J',
        12: 'Q',
        13: 'K'
    }

    card_suit_visual = {
        "heart": "♥",
        "spade": "♠",
        "club": "♣",
        "diamond": "♦"
    }

    def __init__(self, val, suit):
        self.val = val
        self.suit = suit
        self.card_string = self.to_string()
        self.calc_val = self.set_calc_val(val)
    
    def set_calc_val(self, val):
        if val == 1:
            return 11
        if val > 10:
            return 10
        return val

        



    def to_string(self):
        card_str = ""
        if self.val in Card.card_value_visual.keys():
            card_str = Card.card_value_visual[self.val]
        else:
            card_str = str(self.val)
        
        card_str = card_str + " " + Card.card_suit_visual[self.suit]
        return card_str 
        



