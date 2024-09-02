
class Player:

    count = 0

    def __init__(self, name) -> None:
        Player.count = Player.count + 1
        self.no = str(Player.count)
        self.cards = []
        self.name = name

    def add_card(self, card):
        self.cards.append(card)

    def get_sum(self):
        sum = 0
        ace_exists = False
        ace_count = 0
        for card in self.cards:
            if card.val == 1:
                ace_count += 1

            sum = sum + card.calc_val
        
        while ace_count > 0:
            if sum > 21:
                sum = sum - 10
            ace_count -= 1
        


        return sum
