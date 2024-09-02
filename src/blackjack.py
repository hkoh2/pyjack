# from lib.card import Card
from utils.table import Table
from utils.player import Player
from utils.dealer import Dealer

new_dealer = Player("Dealer")
player_1 = Player("John")
player_2 = Player("Dave")
player_3 = Player("Matt")
player_4 = Player("Sean")
players = [player_1, player_2, player_3, player_4]

new_table = Table(new_dealer, players)


new_table.play()

