from setting import stack, small_blind, big_blind
from datetime import datetime
import time
import dictionary
import random 

def declare_important_variables():
#Определение важных переменных
# raik = 0.05 # Переменная рейк этого казино
  stack = 100000 # закуп игроков. Используется в словаре money
  small_blind = stack // 200 # малый блайнд
  big_blind = stack // 100 # большой блайнд 

def g_time():
  data = datetime.fromtimestamp(time.time()).strftime("%d.%m.%Y %H:%M:%S")
  print(data)

def welcome():
  print(dictionary.personal["NAME VLADELEC GAME"], dictionary.Welcome["MESSAGE ONE"])
  print(dictionary.Welcome["MESSAGE TWO"])

def players_seat():
  # Игроки садятся за стол
  print(dictionary.Welcome["MESSAGE THREE"])
  Players = []
  n = 0
  while not(n >= 2 and n <= 9):
    print("Введите количество игроков. От 2 до 9")
    n = int(parsing(input()))
  print("Введите имена игроков, в конце введите End")
  for i in range(n):
    Players.append(input())
  return Players
  # Игроки сели, их имена лежат в Players

def long_table(Players):
  N = len(Players)
  return N

def message_four():
  print(dictionary.Welcome["MESSAGE FOUR"])

def detected_button(Players):
# Определяем баттон
  k = 0
  BUTTON = 0
  while not(k == 1):
    k = 0
    print("Определяем баттон")
    deck = start_deck()
    deck_haos = haos(deck)
    cards = {}
    i = 0
    for item in Players:
      cards[item] = [deck_haos[i]]
      i += 1
    print(cards)
    high_value_card = 0
    button = []
    cards_value = {}
    for item in cards:
      if (cards[item][0][0] == 'A') or (cards[item][0][0] == 'K') or (cards[item][0][0] == 'Q') or (cards[item][0][0] == 'J') or (cards[item][0][0] == 'T'):
        if cards[item][0][0] == 'A':
          cards_value[item] = dictionary.power_cards["A"]
        if cards[item][0][0] == 'K':
          cards_value[item] = dictionary.power_cards["K"]
        if cards[item][0][0] == 'Q':
          cards_value[item] = dictionary.power_cards["Q"]
        if cards[item][0][0] == 'J':
          cards_value[item] = dictionary.power_cards["J"]
        if cards[item][0][0] == 'T':
          cards_value[item] = dictionary.power_cards["T"]
      else:
        cards_value[item] = int(cards[item][0][0])
    for item in cards_value:
      if cards_value[item] > high_value_card:
        high_value_card = cards_value[item]
        button = item
    for item in cards_value:
      if cards_value[item] == high_value_card:
        k += 1
    j = 0
    for item in Players:
      if item == button:
        BUTTON = j
      j += 1
  Players_seat = Players[BUTTON:] + Players[:BUTTON]
  return Players_seat

def detected_position(Players_seat):
# Создаем словарь позиций
  position = {}
  if len(Players_seat) == 2:
    position[Players_seat[0]] = [dictionary.position_HU["BUTTON, SMALL BLIND"]]
    position[Players_seat[1]] = [dictionary.position_6_max["BIG BLIND"]]
  if len(Players_seat) > 2:
    position[Players_seat[0]] = [dictionary.position_6_max["BUTTON"]]
    position[Players_seat[1]] = [dictionary.position_6_max["SMALL BLIND"]]
    position[Players_seat[2]] = [dictionary.position_6_max["BIG BLIND"]]
    if len(Players_seat) <= 6:
      if len(Players_seat) == 4:
        position[Players_seat[3]] = [dictionary.position_6_max["CATT OFF"]]
      if len(Players_seat) == 5:
        position[Players_seat[3]] = [dictionary.position_6_max["MIDDLE POSITION"]]
        position[Players_seat[4]] = [dictionary.position_6_max["CATT OFF"]]
      if len(Players_seat) == 6:
        position[Players_seat[3]] = [dictionary.position_6_max["EARLY POSITION"]]
        position[Players_seat[4]] = [dictionary.position_6_max["MIDDLE POSITION"]]
        position[Players_seat[5]] = [dictionary.position_6_max["CATT OFF"]]
    if (len(Players_seat) > 6) and (len(Players_seat) <= 9):
      if len(Players_seat) == 7:
        position[Players_seat[3]] = [dictionary.position_Full_Ring["UNDER THE GUN 1"]]
        position[Players_seat[4]] = [dictionary.position_Full_Ring["UNDER THE GUN 2"]]
        position[Players_seat[5]] = [dictionary.position_Full_Ring["UNDER THE GUN 3"]]
        position[Players_seat[6]] = [dictionary.position_Full_Ring["MIDDLE POSITION 1"]]
      if len(Players_seat) == 8:
        position[Players_seat[3]] = [dictionary.position_Full_Ring["UNDER THE GUN 1"]]
        position[Players_seat[4]] = [dictionary.position_Full_Ring["UNDER THE GUN 2"]]
        position[Players_seat[5]] = [dictionary.position_Full_Ring["UNDER THE GUN 3"]]
        position[Players_seat[6]] = [dictionary.position_Full_Ring["MIDDLE POSITION 1"]]
        position[Players_seat[7]] = [dictionary.position_Full_Ring["MIDDLE POSITION 2"]]
      if len(Players_seat) == 9:
        position[Players_seat[3]] = [dictionary.position_Full_Ring["UNDER THE GUN 1"]]
        position[Players_seat[4]] = [dictionary.position_Full_Ring["UNDER THE GUN 2"]]
        position[Players_seat[5]] = [dictionary.position_Full_Ring["UNDER THE GUN 3"]]
        position[Players_seat[6]] = [dictionary.position_Full_Ring["MIDDLE POSITION 1"]]
        position[Players_seat[7]] = [dictionary.position_Full_Ring["MIDDLE POSITION 2"]]
        position[Players_seat[8]] = [dictionary.position_Full_Ring["CATT OFF"]]
  print(dictionary.message["POSITION"], position)
  return position

def message_five():
  print(dictionary.Welcome["MESSAGE FIVE"])

def by():
  print(dictionary.message["ALL END BYIN"])

def profit(Players_seat):
# Создаем словарь profit
  profit = {}
  for item in Players_seat:
    profit[item] = 0
  print(dictionary.message["PROFIT"], profit)
  return profit

def start_deck():
# Формирует колоду
  cards = ["A", "K", "Q","J","T","9","8","7","6","5","4","3","2"]
  tsdh = ["t", "s", "d", "h"]
  deck = []
  for i in cards:
    for j in tsdh:
      deck.append(i + j)
  return deck

def haos(deck):
# Перемешивает колоду
  print(dictionary.message["STATUS DECK ONE"])
  s1 = []
  s2 = []
  s3 = []
  deck_haos = deck
  for i in range(120):
    k = random.randint(0, 51)
    l = random.randint(k, 51)
    s1 = deck_haos[:k]
    s2 = deck_haos[k:l]
    s3 = deck_haos[l:]
    deck_haos = s2 + s1 + s3
  print(dictionary.message["STATUS DECK TWO"])
  return deck_haos

def money(Players_seat):
# Создает словарь денег
  money = {}
  for item in Players_seat:
    money[item] = stack
  print(dictionary.message["MONEY"], money)
  return money

def parsing(answer):
## Функция парсинг ответа на предмет выбирания из него цифр
  pars_answer = ""
  for item in answer:
    for i in range(10):
      if item == str(i):
        pars_answer = pars_answer + item
  if pars_answer == "":
    pars_answer = "1"
  return pars_answer

def info(info):
  if info == "info":
    for item in dictionary.combination:
      print(dictionary.combination[item])

def folds_or_no(item, Players_folds):
  folds = 0
  for i in range(len(Players_folds)):
    if item == Players_folds[i]:
      folds = 1
      break
  return folds

def who_is_her(Players_seat, Players_folds):
  quan = len(Players_seat)
  for i in range(len(Players_seat)):
    for j in range(len(Players_folds)):
      if Players_seat[i] == Players_folds[j]:
        quan -= 1
  return quan

def blinds(
  Players_seat, position, money, 
  small_blind ,big_blind, bank,
  position_HU, 
  position_Full_Ring, 
  message, 
  USD
  ):
# Простановка блайндов  
  for item in Players_seat:
    if ((position[item] == [dictionary.position_HU["BUTTON, SMALL BLIND"]]) 
      or (position[item] == [dictionary.position_Full_Ring["SMALL BLIND"]])):
      money[item] = money[item] - small_blind
      bank = bank + small_blind
      action_blinds.append([item, position[item][0], dictionary.message["BET SMALL BLINDS"], small_blind])
      print(action_blinds)
      print(dictionary.personal["DEALER"], item, dictionary.message["BET SMALL BLINDS"], small_blind, dictionary.USD["$"])
    if position[item] == [dictionary.position_Full_Ring["BIG BLIND"]]:
      money[item] = money[item] - big_blind
      bank = bank + big_blind
      action_blinds.append([item, position[item][0], dictionary.message["BET BIG BLINDS"], big_blind])
      print(action_blinds)
      print(dictionary.personal["DEALER"], item, dictionary.message["BET BIG BLINDS"], big_blind, dictionary.USD["$"])
      print(money, dictionary.message["BANK"], bank)
  return money, bank, action_blinds

def cards_down(Players_seat):
#Раздаем карты
  i = 0
  for item in Players_seat:
    cards[item] = [deck_haos[i], deck_haos[i+n]]
    i += 1
  print(cards)
  print(dictionary.message[" Игроки получили свои карты "])
  print(" Никому не показывайте свои карты, даже если человек представляется сотрудником Вашего Банка!")
  return cards

def write_move():
#Запрашивает ответ игрока
  answer = input()
  function.info(answer)
  answer = int(function.parsing(answer))
  return answer

def get_answer_check(big_blind, money, item):
  print(dictionary.personal["DEALER"], dictionary.message["ACTION TO PLAYER"], item)
  answer = -1
  if not((answer == 0)
    or ((answer >= big_blind) 
    and (answer <= money[item]) 
    and answer % big_blind == 0)):
    while not((answer == 0) 
      or ((answer >= big_blind) 
      and (answer <= money[item])
      and answer % big_blind == 0)):
      print(
        dictionary_of_personal["DEALER"], dictionary.message["BANK"], bank, dictionary.USD["$"], 
        dictionary.message["YOUR NONEY"], money[item], USD["$"], dictionary.message["YOUR POSITION"], 
        position[item][0], dictionary.message["YOUR CARDS"], cards[item], item, dictionary.message["ENTER"], 
        to_call, dictionary.USD["$"], dictionary.action["TO CHECK"], dictionary.action["MIN"], big_blind, 
        USD["$"],dictionary.action["TO BET"]
        )
    answer = write_move()
    return answer

def get_answer_check(big_blind, money, item):
  print(dictionary.personal["DEALER"], dictionary.message["ACTION TO PLAYER"], item)
  answer = -1
  if not((answer == 0)
    or ((answer >= big_blind) 
    and (answer <= money[item]) 
    and answer % big_blind == 0)):
    while not((answer == 0) 
      or ((answer >= big_blind) 
      and (answer <= money[item])
      and answer % big_blind == 0)):
      print(
        dictionary_of_personal["DEALER"], dictionary.message["BANK"], bank, dictionary.USD["$"], 
        dictionary.message["YOUR NONEY"], money[item], USD["$"], dictionary.message["YOUR POSITION"], 
        position[item][0], dictionary.message["YOUR CARDS"], cards[item], item, dictionary.message["ENTER"], 
        to_call, dictionary.USD["$"], dictionary.action["TO CHECK"], dictionary.action["MIN"], big_blind, 
        USD["$"],dictionary.action["TO BET"]
        )
    answer = write_move()
  return answer

def action_preflop(position, money, Players_seat):
# Инициаиция игры!!!!!!!
  bank = 0 # Переменная банк
  action_blinds = [["Blinds"]] # Истинный Список дейстий блайнды
  action_preflop = [["Preflop"]] # Список действий префлоп
  Players_folds = []
  to_call = big_blind # Сумма, которую надо заколлировать игроку
  answer = big_blind # Ответ игрока
  k = -1 # количество кругов торговли
  ishod = 0
  summ = 0
  money_in_game = 0
  last_raise = big_blind
  last_raise_item_preflop = 0
  print("***Dealing Blinds***")
# Ход игры   
  print(action_blinds)
  print("***Dealing Preflop***")
  print(dictionary.message["POSITION"], position)
  while not(ishod == 1):
    k += 1
    for item in Players_seat:
      fold = function.folds_or_no(item, Players_folds)
      if fold == 0:
        to_call = last_raise - ( stack - money[item] )
        if to_call == 0:
          if position[item] == [dictionary.position_Full_Ring["BIG BLIND"]] and k == 0:
            pass
          else:
            answer = get_answer_check(big_blind, money[item])
            if answer == 0:
              action_preflop.append([item, position[item][0], dictionary.message["TO CHECK"]])
              print(action_preflop)
              print(dictionary.personal["DEALER"], item, position[item][0], dictionary.message["TO CHECK"])
            else:
              if position[item] == [dictionary.position_Full_Ring["BIG BLIND"]] and k == 1:
                money[item] = money[item] - answer + big_blind
              if (position[item] == [dictionary.position_Full_Ring["SMALL BLIND"]] 
                or position[item] == [dictionary.position_HU["BUTTON, SMALL BLIND"]]
                and k == 1):
                money[item] = money[item] - answer + small_blind
              if not((position[item] == [dictionary.position_Full_Ring["BIG BLIND"]] 
                or position[item] == [dictionary.position_Full_Ring["SMALL BLIND"]] 
                or position[item] == [dictionary.position_HU["BUTTON, SMALL BLIND"]]) 
                and k == 1):
                for i in action_preflop:
                  if i == ["Preflop"]:
                    pass
                  else:
                    if i[0] == item and i[2] == "Raises":
                      last_raise_item_preflop = i[3]
                  money[item] = money[item] - answer + last_raise_item_preflop
                  bank = bank + answer
                if money[item] == 0:
                  action_preflop.append([item, position[item][0], dictionary.message["TO BET"], answer])
                  print(action_preflop)
                  print(dictionary.personal["DEALER"], item, position[item][0], 
                  dictionary.message["TO BET ALL IN"], answer, dictionary.USD["$"])
                else:
                  action_preflop.append([item, position[item][0], dictionary.message["TO BET"], answer])
                  print(action_preflop)
                  print(dictionary.personal["DEALER"], item, dictionary.position[item][0], 
                  dictionary.message["TO BET"], answer, dictionary.USD["$"])
                  last_raise = answer
        else:
# Если to_call не равен нулю
            if ((k == 0) 
              and ((position[item] == [dictionary.position_HU["BUTTON, SMALL BLIND"]]) 
              or (position[item] == [dictionary.position_6_max["SMALL BLIND"]]) 
              or (position[item] == [dictionary.position_6_max["BUTTON"]]))):
              pass
            else:
              answer = get_answer_bet(big_blind, money, item)
              if answer == 0:
                action_preflop.append([item, position[item][0], dictionary.message["TO FOLD"]])
                Players_folds.append(item)
                print(action_preflop)
                print(dictionary.personal["DEALER"], item, position[item][0], 
                dictionary.message["TO FOLD"])
              else:
                if answer == to_call:
                  money[item] = money[item] - to_call
                  bank = bank + to_call
                  action_preflop.append([item, position[item][0], dictionary.message["TO CALL"], to_call])
                  print(action_preflop)
                  print(dictionary.personal["DEALER"], item, position[item][0], 
                  dictionary.message["TO CALL"], to_call, dictionary.USD["$"])
                else:
                  if ((position[item] == [dictionary.position_Full_Ring["SMALL BLIND"]] 
                     or position[item] == [dictionary.position_HU["BUTTON, SMALL BLIND"]]) 
                     and k == 1):
                    money[item] = money[item] - answer + small_blind
                  if position[item] == [dictionary.position_Full_Ring["BIG BLIND"]] and k == 1:
                    money[item] = money[item] - answer + big_blind
                  if (not(k == 1 and (position[item] == [dictionary.position_Full_Ring["SMALL BLIND"]] 
                    or position[item] == [dictionary.position_Full_Ring["BIG BLIND"]] 
                    or (position[item] == [dictionary.position_HU["BUTTON, SMALL BLIND"]])))):
                    for i in action_preflop:
                      if i == ["Preflop"]:
                        pass
                      else:
                        if i[0] == item and i[2] == "Raises":
                          last_raise_item_preflop = i[3]
                    money[item] = money[item] - answer + last_raise_item_preflop
                    bank = bank + answer
                  if money[item] == 0:
                    action_preflop.append([item, position[item][0], dictionary.message["TO RAISE"], answer])
                    print(action_preflop)
                    print(dictionary.personal["DEALER"], item, position[item][0], dictionary.message["TO RAISE ALL IN"], answer, dicitinary.USD["$"])
                  else:
                    action_preflop.append([item, position[item][0], dictionary.message["TO RAISE"], answer])
                    print(action_preflop)
                    print(
                    dictionary.personal["DEALER"], item, position[item][0], 
                    dictionary.message["TO RAISE"], answer, dictionary.USD["$"]
                    )
                    last_raise = answer
        if function.who_is_her(Players_seat, Players_folds) == 1: break
        ishod = 1
        fold = 0
        item_copy = item
        for item in Players_seat:
          fold = function.folds_or_no(item, Players_folds)
          if fold == 0:
            if (stack - money[item]) > money_in_game:
              money_in_game = stack - money[item]
        for item in Players_seat:
          fold = function.folds_or_no(item, Players_folds)
          if fold == 0:
            if (stack - money[item]) == money_in_game:
              pass
            else:
              ishod += 1
        item = item_copy
        if k == 1 and last_raise == big_blind:
          if (ishod == 1):
           if position[item] == [dictionary.position_6_max["BIG BLIND"]]: break
        if k >= 1 and answer > big_blind:
          if (ishod == 1): break
      print(action_preflop)
      return money, bank, action_preflop

def flop_down(N):
  flop = []
  for i in range(3):
     flop.append(function.deck_haos[2 * N + 1 + i])
  print(dictionary.personal["DEALER"], "Flop", flop)
  return flop

def money_flop():
  for item in Players_seat:
    fold = function.folds_or_no(item, Players_folds)
    if fold == 0:
      money_flop = money[item]
  return money_flop
      
def flop_round(Players_seat, Players_folds, money):
  action_flop = [["Flop"]] # Список действий префлоп
  to_call = -1 # Сумма, которую надо заколлировать игроку
  answer = 0 # Ответ игрока
  k = -1 # количество кругов торговли
  ishod = len(Players_seat)
  last_raise = 0
  money_in_game = 0
  last_raise_item_flop = 0

  if not(function.who_is_her(Players_seat, Players_folds) == 1) and not(money_in_game == stack):
    while not(ishod == 1 and k >= 1):
      k += 1
      for item in Players_seat:
        fold = function.folds_or_no(item, Players_folds)
        if fold == 0:
          to_call = last_raise - ( money_flop - money[item] )
          if to_call == 0:
            if position[item] == [dictionary.position_Full_Ring["BUTTON"]] and k == 0:
              pass
            else:
              answer = get_answer_check(big_blind, money[item])
              if answer == 0:
                action_flop.append([item, dictionary.message["TO CHECK"]])
                print(action_flop)
                print(dictionary.personal["DEALER"], item, position[item][0], 
                dictionary.message["TO CHECK"])
              else:
                for i in action_flop:
                  if i == ["Flop"]:
                    pass
                  else:
                      if i[0] == item and i[2] == "Raises":
                        last_raise_item_flop = i[3]
                  money[item] = money[item] - answer + last_raise_item_flop
                  bank = bank + answer
                  if money[item] == 0:
                    action_flop.append([item, dictionary.message["TO BET"], answer])
                    print(action_flop)
                    print(dictionary.personal["DEALER"], item, position[item][0], dictionary.message["TO BET ALL IN"], answer, dictionary.USD["$"])
                  else:
                    action_flop.append([item, dictionary.message["TO BET"], answer])
                    print(action_flop)
                    print(dictionary.personal["DEALER"], item, position[item][0], dictionary.message["TO BET"], answer, dictionary.USD["$"])
                  last_raise = answer
          else:
                if (k == 0) and (position[item] == [dictionary.position_Full_Ring["BUTTON"]]):
                  pass
                else:
                  answer = get_answer_bet(big_blind, money, item)
                  if answer  == 0:
                    action_flop.append([item, dictionary.message["TO FOLD"]])
                    Players_folds.append(item)
                    print(action_flop)
                    print(dictionary.personal["DEALER"], item, position[item][0], dictionary.message["TO FOLD"])
                  else:
                    if answer == to_call:
                      money[item] = money[item] - to_call
                      bank = bank + to_call
                      action_flop.append([item, dictionary.message["TO CALL"], to_call])
                      print(action_flop)
                      print(dictionary.personal["DEALER"], item, position[item][0], dictionary.message["TO CALL"], to_call, dcitionary.USD["$"])
                    else:
                      for i in action_flop:
                        if i == ["Flop"]:
                          pass
                        else:
                          if i[0] == item and i[2] == "Raises":
                            last_raise_item_flop = i[3]
                    money[item] = money[item] - answer + last_raise_item_flop
                    bank = bank + answer
                    if money[item] == 0:
                      action_flop.append([item, position[item][0], dictionary.message["TO RAISE"], answer])
                      print(action_flop)
                      print(dictionary_of_personal["DEALER"], item, dictionary.message["TO RAISE ALL IN"], answer, dictionary.USD["$"])
                    else:
                      action_flop.append([item, position[item][0], dictionary.message["TO RAISE"], answer])
                      print(action_flop)
                      print(dictionary_of_personal["DEALER"], item, position[item][0], dictionary.message["TO RAISE"], answer, dictionary.USD["$"])
                    last_raise = answer
      ishod = 1
      fold = 0
      item_copy = item
      for item in Players_seat:
        fold = function.folds_or_no(item, Players_folds)
        if fold == 0:
          if (money_flop - money[item]) > money_in_game:
            money_in_game = money_flop - money[item]
      for item in Players_seat:
        fold = function.folds_or_no(item, Players_folds)
        if fold == 0:
          if (money_flop - money[item]) == money_in_game:
            pass
          else:
            ishod += 1
      item = item_copy
      if k == 1:
        if ishod == 1 and position[item] == [dictionary.position_6_max["BUTTON"]]: 
          break
      if k >= 2:
        if ishod == 1: break

      print(action_flop)
  return bank, money, action_flop

def turn_round(Players_seat, Players_folds, money, N):
  print("***Dealing Turn***")
  print(dictionary.message["POSITION"], position)
  print(dictionary.personal["DEALER"], money, dictionary.message["BANK"], bank, dictionary.USD["$"])

  turn = fucntion.deck_haos[2 * N + 5 + i]
  board.append(turn)
  print(dictionary.personal["DEALER"], "Turn", board)

  for item in Players_seat:
    fold = function.folds_or_no(item, Players_folds)
    if fold == 0:
      money_turn = money[item]
  action_turn = [["Turn"]] # Список действий префлоп
  to_call = -1 # Сумма, которую надо заколлировать игроку
  answer = 0 # Ответ игрока
  k = -1 # количество кругов торговли
  ishod = len(Players_seat)
  last_raise = 0
  money_in_game = 0
  last_raise_item_turn = 0

  if not(function.who_is_her(Players_seat, Players_folds) == 1) and not(money_in_game == stack):
    while not(ishod == 1 and k >= 1):
      k += 1
      for item in Players_seat:
        fold = function.folds_or_no(item, Players_folds)
        if fold == 0:
          to_call = last_raise - ( money_turn - money[item] )
          if to_call == 0:
            if position[item] == [dictionary.position_Full_Ring["BUTTON"]] and k == 0:
              pass
            else:
              answer = get_answer_check()
              if answer  == 0:
                action_turn.append([item, dictionary.message["TO CHECK"]])
                print(action_preflop)
                print(dictionary.personal["DEALER"], item, position[item][0], dictionary.message["TO CHECK"])
              else:
                for i in action_turn:
                  if i == ["Turn"]:
                    pass
                  else:
                    if i[0] == item and i[2] == "Raises":
                      last_raise_item_turn = i[3]
                    money[item] = money[item] - answer + last_raise_item_turn
                    bank = bank + answer
                  if money[item] == 0:
                    action_turn.append([item, dictionary.message["TO BET"], answer])
                    print(action_turn)
                    print(dictionary.personal["DEALER"], item, position[item][0], 
                    dictionary.message["TO RAISE ALL IN"], answer, dictionary.USD["$"])
                  else:
                    action_turn.append([item, dictionary.message["TO BET"], answer])
                    print(action_turn)
                    print(dictionary.personal["DEALER"], item, position[item][0], 
                    dictionary.message["TO BET"], answer, dictionary.USD["$"])
                  last_raise = answer
                  last_raiser_turn = item 
          else:
                if ((k == 0) 
                  and (position[item] == [dictionary.position_Full_Ring["BUTTON"]])):
                  pass
                else:
                  answer = get_answer_bet()
                  if answer  == 0:
                    action_turn.append([item, dictionary.message["TO FOLD"]])
                    Players_folds.append(item)
                    print(action_turn)
                    print(dictionary.personal["DEALER"], item, position[item][0], dictionary.message["TO FOLD"])
                  else:
                    if answer == to_call:
                      money[item] = money[item] - to_call
                      bank = bank + to_call
                      action_turn.append([item, dictionary.message["TO CALL"], to_call])
                      print(dictionary.personal["DEALER"], item, position[item][0], 
                      dictionary.message["TO CALL"], to_call, dictionary.USD["$"])
                    else:
                      for i in action_turn:
                        if i == ["Turn"]:
                          pass
                        else:
                          if i[0] == item and i[2] == "Raises":
                            last_raise_item_turn = i[3]
                      money[item] = money[item] - answer + last_raise_item_turn
                      bank = bank + answer
                      if money[item] == 0:
                        action_turn.append([item, position[item][0], dictionary.message["TO RAISE"], answer])
                        print(action_turn)
                        print(dictionary.personal["DEALER"], item, position[item][0], 
                        dictionary.message["TO RAISE ALL IN"], answer, dictionary.USD["$"])
                      else:
                        action_turn.append([item, position[item][0], dictionary.message["TO RAISE"], answer])
                        print(action_turn)
                        print(dictionary.personal["DEALER"], item, position[item][0], 
                        dictionary.message["TO RAISE"], answer, dictionary.USD["$"])
                      last_raise = answer
      ishod = 1
      fold = 0
      item_copy = item
      for item in Players_seat:
        fold = function.folds_or_no(item, Players_folds)
        if fold == 0:
          if (money_turn - money[item]) > money_in_game:
            money_in_game = money_turn - money[item]
      for item in Players_seat:
        fold = function.folds_or_no(item, Players_folds)
        if fold == 0:
          if (money_turn - money[item]) == money_in_game:
            pass
          else:
            ishod += 1
      item = item_copy
      if k == 1:
        if ishod == 1 and position[item] == [dictionary.position_6_max["BUTTON"]]: break
      if k >= 2:
        if ishod == 1: break
  return bank, money, Players_seat

def river_round(Players_seat, Players_folds, money, N):
  print("***Dealing River***")
  print(dictionary_of_message["POSITION"], position)
  print(dictionary_of_personal["DEALER"], money, dictionary.message["BANK"], bank, dictionary.USD["$"])

  river = function.deck_haos[2 * N + 7 + i]
  board.append(river)
  print(dictionary.personal["DEALER"], "River", board)

  for item in Players_seat:
    fold = function.folds_or_no(item, Players_folds)
    if fold == 0:
      money_river = money[item]
  action_river = [["River"]] # Список действий префлоп
  to_call = -1 # Сумма, которую надо заколлировать игроку
  answer = 0 # Ответ игрока
  k = -1 # количество кругов торговли
  ishod = len(Players_seat)
  action_shows = {}
  last_raise = 0
  money_in_game = 0
  last_raise_item_river = 0
  
  if (not(function.who_is_her(Players_seat, Players_folds) == 1) 
    and not(money_in_game == stack)):
    while not(ishod == 1 and k >= 1):
      k += 1
      for item in Players_seat:
        fold = function.folds_or_no(item, Players_folds)
        if fold == 0:
          to_call = last_raise - ( money_river - money[item] )
          if to_call == 0:
            if position[item] == [dictionary.position_Full_Ring["BUTTON"]] and k == 0:
              pass
            else:
              answer = get_answer_check()
              if answer  == 0:
                action_river.append([item, dictionary.message["TO CHECK"]])
                print(action_preflop)
                print(dictionary.personal["DEALER"], item, position[item][0], dictionary.message["TO CHECK"])
              else:
                for i in action_river:
                  if i == ["River"]:
                    pass
                  else:
                      if i[0] == item and i[2] == "Raises":
                        last_raise_item_river = i[3]
              money[item] = money[item] - answer + last_raise_item_river
              bank = bank + answer
              if money[item] == 0:
                action_river.append([item, dictionary.message["TO BET"], answer])
                print(action_river)
                print(dictionary.personal["DEALER"], item, position[item][0], dictionary.message["TO RAISE ALL IN"], answer, dictionary.USD["$"])
              else:
                action_river.append([item, dictionary.message["TO BET"], answer])
                print(action_river)
                print(dictionary.personal["DEALER"], item, position[item][0], dictionary.message["TO BET"], answer, dictionary.USD["$"])
              last_raise = answer
          else:
                if (k == 0) and (position[item] == [dictionary.position_Full_Ring["BUTTON"]]):
                  pass
                else:
                  answer = get_answer_bet()
                  if answer  == 0:
                    action_river.append([item, dictionary.message["TO FOLD"]])
                    Players_folds.append(item)
                    print(action_river)
                    print(dictionary.personal["DEALER"], item, position[item][0], dictionary.message["TO FOLD"])
                  else:
                    if answer == to_call:
                      money[item] = money[item] - to_call
                      bank = bank + to_call
                      action_river.append([item, dictionary.message["TO CALL"], to_call])
                      print(action_river)
                      print(dictionary.personal["DEALER"], item, position[item][0], dictionary.message["TO CALL"], to_call, dictionary.USD["$"])
                    else:
                      for i in action_river:
                        if i == ["River"]:
                          pass
                        else:
                          if i[0] == item and i[2] == "Raises":
                            last_raise_item_river = i[3]
                      money[item] = money[item] - answer + last_raise_item_river
                      bank = bank + answer
                      if money[item] == 0:
                        action_river.append([item, position[item][0], dictionary.message["TO RAISE"], answer])
                        print(action_river)
                        print(dictionary.personal["DEALER"], item, dictionary.message["TO RAISE ALL IN"], answer, dictionary.USD["$"])
                      else:
                        action_river.append([item, position[item][0], dictionary.message["TO RAISE"], answer])
                        print(action_river)
                        print(dictionary.personal["DEALER"], item, dictionary.message["TO RAISE"], answer, dictionary.USD["$"])
                      last_raise = answer
      ishod = 1
      fold = 0
      item_copy = item
      for item in Players_seat:
        fold = function.folds_or_no(item, Players_folds)
        if fold == 0:
          if (money_river - money[item]) > money_in_game:
            money_in_game = money_river - money[item]
      for item in Players_seat:
        fold = function.folds_or_no(item, Players_folds)
        if fold == 0:
          if (money_river - money[item]) == money_in_game:
            pass
          else:
            ishod += 1
      item = item_copy
      if k == 1:
        if ishod == 1 and position[item] == [dictionary.position_6_max["BUTTON"]]: break
      if k >= 2:
         if ishod == 1: break
  return bank, money, Players_seat

def show_down(Players_seat, Players_folds):
  if who_is_her(Players_seat, Players_folds) > 1:
    print("***Show Down***")
    for item in Players_seat:
      fold = function.folds_or_no(item, Players_folds)
      if fold == 0:
        action_shows[item] = [dictionary.action["CARDS SHOWS"]]
        print(item, dictionary.action["CARDS SHOWS"], cards[item])

#  print(action_river)
#  print(dictionary.message["POSITION"], position)
#  print(dictionary.personal["DEALER"], money, dictionary.message["BANK"], bank, dictionary.USD["$"])
 
def winner(who_is_her(), folds_or_no(), Players_seat, Players_folds, item, Players_folds:
  if not(who_is_her(Players_seat, Players_folds) > 1):
    for item in Players_seat:
      fold = folds_or_no(item, Players_folds)
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
