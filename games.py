import dictionary
from dictionary import position_HU, position_Full_Ring, message, USD
import function

def games():
  function.declare_important_variables()

  function.g_time()

  function.welcome()

  Players = function.players_seat()

  function.message_four()

  Players_seat = function.detected_button(Players)

  position = function.detected_position(Players_seat)
# Баттон определен. Места игроков за столом в Players_seat

  function.message_five()

# Закуп игроко
  money = function.money(Players_seat)
# Создали. Количесто денег каждого игрока лежит в money

  function.by()

# Создаем словарь profit
  profit = function.profit(Players_seat)

  status = dictionary.status["Go!"]

  print(dictionary.Welcome["MESSAGE SIX"])

  print(dictionary.Welcome["MESSAGE SEVEN"])

  game = 1
#Тут начинается игра-------------------------
  while not(status == dictionary.status["Stop!"]):
    print(dictionary.personal["DEALER"], "Game №", game)
#start and shaffling deck
    deck = function.start_deck()
    deck_haos = function.haos(deck)

#Раздаем карты
    cards = cards_down(Players_seat)

# Простановка блайндов  
    money, bank, action_blinds = blinds(
      Players_seat, position, money, 
      small_blind ,big_blind, bank,
      position_HU, 
      position_Full_Ring, 
      message, USD
      )

    money, bank, action_preflop = function.action_blinds(position, money, Players_seat)
    
    money, bank, action_preflop = function.action_preflop(position, money, Players_seat)
      
    print(action_preflop)
# Блайнды проставлены

    print("***Dealing Flop***")
    print(dictionary.message["POSITION"], position)
    print(dictionary.personal["DEALER"], money, dictionary.message["BANK"], bank, dictionary.USD["$"])
    N = long_table(Players)
    board = function.flop(N)

    money_flop = function.money_flop()

    money, bank, action_preflop = function.action_flop(position, money, Players_seat)

    money, bank, action_preflop = function.action_turn(position, money, Players_seat)

    money, bank, action_preflop = function.action_turn(position, money, Players_seat)

    if who_is_her(Players_seat, Players_folds) > 1:
      print("***Show Down***")
      for item in Players_seat:
        fold = function.folds_or_no(item, Players_folds)
        if fold == 0:
          action_shows[item] = [dictionary.action["CARDS SHOWS"]]
          print(item, dictionary.action["CARDS SHOWS"], cards[item])
  
      print(action_river)
      print(dictionary.message["POSITION"], position)
      print(dictionary.personal["DEALER"], money, dictionary.message["BANK"], bank, dictionary.USD["$"])
  
      if not(function.who_is_her(Players_seat, Players_folds) > 1):
        for item in Players_seat:
          fold = function.folds_or_no(item, Players_folds)
          if fold == 0:
            winner = item
        print("Winner - ",item, "Bank - ", bank)
# Обнуление
      game += 1
      Players_seat = Players[0:] + Players[:0]
      position = detected_position(Players_seat)
      for item in Players_seat:
        money[item] = stack
# Сброс   

    status = input()
