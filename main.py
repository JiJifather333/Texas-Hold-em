import games
from games import combination, nohand_combination, position_HU, action, personal, power_cards, position_6_max, Welcome, status_go, USD, position_Full_Ring, message

stack, small_blind, big_blind, raik = games.declare_important_variables()

games.welcome(personal, Welcome)

n, Players = games.append_players(Welcome)

deck = games.start_deck()

Players_seat = games.who_button(deck, power_cards, Players)

position = games.detected_position(Players_seat)

games.message_four(Welcome)

games.message_five(Welcome)

money = games.money(Players_seat, stack, message)

status, number_game = games.start_game(status_go, Welcome)

games.game(status_go, personal, number_game, Players_seat, n, message, position, position_HU, position_6_max, position_Full_Ring, USD, stack, big_blind, small_blind)


