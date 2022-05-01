from datetime import datetime
import time
import dictionary
import function
import games

#Определение важных переменных
#raik = 0.05 # Переменная рейк этого казино
stack = 100000 # закуп игроков. Используется в словаре money
small_blind = stack // 200 # малый блайнд
big_blind = stack // 100 # большой блайнд 

#ИНИЦИАЛИЗАЦИЯ ИГРЫ------------------------------------------------------

# Пристегните ремни, игра началась!!!

# Время
data = datetime.fromtimestamp(time.time()).strftime("%d.%m.%Y %H:%M:%S")

print(data)
#Время

# Welcome
print(dictionary.personal["NAME VLADELEC GAME"], dictionary.Welcome["MESSAGE ONE"])
print(dictionary.Welcome["MESSAGE TWO"])
# Welcome

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
# Игроки сели, их имена лежат в Players

print(dictionary.Welcome["MESSAGE FOUR"])

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

# Создаем словарь позиций
def detected_position(Players_seat):
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
  return position
position = detected_position(Players_seat)
print(dictionary.message["POSITION"], position)
# Создали. Позиции игроков лежат в position
# Баттон определен. Места игроков за столом в Players_seat

# Закуп игроков

print(dictionary.Welcome["MESSAGE FIVE"])

# Создаем словарь денег
money = {}
for item in Players_seat:
  money[item] = stack
print(dictionary.message["MONEY"], money)
# Создали. Количесто денег каждого игрока лежит в money

print(dictionary.message["ALL END BYIN"])

# Создаем словарь profit
profit = {}
for item in Players_seat:
  profit[item] = 0
print(dictionary.message["PROFIT"], profit)
# Создали. profit каждого игрока лежит в profit
#ИНИЦИАЛИЗАЦИЯ ИГРЫ------------------------------------------------------
# Все закупились

# Начало игры

games.game(Players_seat, position, money, profit, n, stack, small_blind, big_blind)

status = dictionary.status["Go!"]


