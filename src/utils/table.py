
from utils.player import Player
from utils.dealer import Dealer
from utils.deck import Deck

class Table:



    def __init__(self, dealer, players) -> None:
        self.dealer = dealer
        # players are list of players
        self.players = players
        self.all_bust = False
        self.deck = Deck()
    
    def get_table_view(self):
        print("Dealer")
        print(" FACE DOWN")
        print(" " + self.dealer.cards[1].to_string())
        for player in self.players:
            print("Player " + player.name)
            for card in player.cards:
                print(" " + card.to_string())



    def play(self):
        print("Start Play!")
        print("Dealing cards...")
        self.deal_init()
        self.get_table_view()
        self.players_turn()
        
    def deal_init(self):
        self.deal_hands()
        self.deal_hands()
    
    def players_turn(self):
        for player in self.players:
            self.player_action(player)


    def player_action(self, player):
        # hit or hold
        print("---------------------------------------------")
        print("Player " + player.name + " Turn")
        
        bust = False

        choice = 0
        while not bust and choice is not "2":
            self.show_hand(player)
            choice = input("* Hit (1) or Stand (2)?")
            draw = self.deck.pop()
            print("Dealing: " + draw.to_string())
            player.add_card(draw)
            self.show_hand(player)
            total = player.get_sum()
            print("Total: " + str(total))
            if total > 21:
                bust = True
        
        print("Player " + player.name + " BUSTED!")
        print('--- NEXT PLAYER ---')
            



    
    def show_hand(self, player):
        for card in player.cards:
            print(card.to_string())


    def dealer_turn(self):
        pass

    def deal_hands(self) -> None:
        for player in self.players:
            player.add_card(self.deck.pop())
        self.dealer.add_card(self.deck.pop())

    def deal_card(self) -> None:
        pass



    
    def dealer_turn(self):
        pass

    def dealer_turn(self):
        pass
