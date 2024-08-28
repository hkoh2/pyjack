# from lib.card import Card
from lib.table import Table
from lib.player import Player
from lib.dealer import Dealer

new_dealer = Dealer
player_1 = Player
player_2 = Player
player_3 = Player
player_4 = Player
players = [player_1, player_2, player_3, player_4]

new_table = Table(new_dealer, players)


new_table.play()

