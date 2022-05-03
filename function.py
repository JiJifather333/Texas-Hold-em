from datetime import datetime
import time
import dictionary
import random 

def famous_variable():
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
    n = int(function.parsing(input()))
  print("Введите имена игроков, в конце введите End")
  for i in range(n):
    Players.append(input())
  return Players
  # Игроки сели, их имена лежат в Players

def message_four():
  print(dictionary.Welcome["MESSAGE FOUR"])

def decteted_button(Players):
# Определяем баттон
  k = 0
  BUTTON = 0
  while not(k == 1):
    k = 0
    print("Определяем баттон")
    deck = function.start_deck()
    deck_haos = function.haos(deck)
    cards = {}
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

def money(Players_seat):
# Создает словарь денег
  money = {}
  for item in Players_seat:
    money[item] = stack
  print(dictionary.message["MONEY"], money)
  return money

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
