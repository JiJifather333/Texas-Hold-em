
#raik = 0.05 # Переменная рейк этого казино
stack = 100000 # закуп игроков. Используется в словаре money
small_blind = stack // 200 # малый блайнд
big_blind = stack // 100 # большой блайнд


# Формируем колоду
def start_deck():
  cards = ["A", "K", "Q","J","T","9","8","7","6","5","4","3","2"]
  tsdh = ["t", "s", "d", "h"]
  deck = []
  for i in cards:
    for j in tsdh:
      deck.append(i + j)
  return deck
# Колода готова. Лежит в deck

# Определяем навания покерных комбинаций
dictionary_of_combination = {"Royal Flush":"Royal Flush  Ex.: As Ks Qs Js Ts","Street Flush":"Street Flush Ex.: Js Ts 9s 8s 7s","Kare":"Kare         Ex.: As Ad Ah At 2h","Full Haus":"Full Haus    Ex.: As Ad Ah Ks Kh","Flush":"Flush        Ex.: As Ks 7s 5s 2s","Street":"Street       Ex.: 9t 8s 7d 6h 5s", "Set":"Set          Ex.: As Ad Ah 4h 7s","Two Pair":"Two Pair     Ex.: As Ad Ks Kh 5t","Pair":"Pair         Ex.: As Ad Tt 6h 3d", "High card":"High Card    Ex.: Ks 9s 7d 4t 3h"}

dictionary_nohand_combination = {"Street Draw":"Street Draw","Flush Draw":"Flush Draw", "Backdoor Street Draw":"Backdoor Street Draw", "Backdoor Flush":"Backdoor Flush", "Two OverCard":"Two OverCard", "One OverCard":"One OverCard","Nothing":"Nothing"}

dictionary_of_position_HU = {"BUTTON, SMALL BLIND":"BTN, SB", "BIG BLIND":"BIG BLIND"}

dictionary_of_action = {"MIN":"Кратно",  "TO FOLD":"Fold", "TO CALL":"Call", "TO RAISE":"Raise",  "TO CHECK":"Check", "TO BET":"Bet", "CARDS SHOWS":"Cards shows", "TO BET ALL IN":"TO bet all in"}

dictionary_of_personal = {"NAME VLADELEC GAME": "NIKITA CHERNOV", "DEALER":"DEALER:"}
power_cards = {"A":13, "K":12, "Q":11, "J":10, "T":9, "7": 7, "6": 6, "5": 5, "4": 4, "3": 3, "2": 2}

dictionary_of_position_6_max = {"EARLY POSITION":"EP","MIDDLE POSITION":"MP","CATT OFF":"CO","BUTTON":"BTN","SMALL BLIND":"SB","BIG BLIND":"BB"}

Welcome = {"MESSAGE ONE": " Добро пожаловать в самое прекрасное казино на свете CherCasino! CherCasino - деньги в корзину. Try your luck!", "MESSAGE TWO":"Стоп слово - Stop! Да да, не удивляйтесь", "MESSAGE THREE": " ++++ Игроки садятся за стол ++++", "MESSAGE FOUR":" ++++ Игроки сели за стол ++++", "MESSAGE FIVE":" by-in 100.000 $", "MESSAGE SIX":" Пристегните ремни, игра началась!!!", "MESSAGE SEVEN":" Если вы или ваши близкие страдают от игровой зависимости мы бы порекомендовали вам выйти из за стола. Но теперь каждый из вас покинет стол только если он пустой или мертвый. Удачи!"}

dictionary_of_status = {"Go!": "Go!","Stop!":"Stop!"}

USD = {"$":"$"}
dictionary_of_position_Full_Ring = {"UNDER THE GUN 1":"UTG 1", "UNDER THE GUN 2":"UTG 2", "UNDER THE GUN 3":"UTG 3", "MIDDLE POSITION 1":"MP 1", "MIDDLE POSITION 2":"MP 2", "CATT OFF":"CO", "BUTTON":"BTN","SMALL BLIND":"SB","BIG BLIND":"BB"}

dictionary_of_message = {"YOUR CARDS": "your cards:","ENTER":"ENTER","BET SMALL BLINDS":"posts small blind","BET BIG BLINDS":"posts big blind" ,"YOUR NONEY":"Your money","YOUR POSITION":"Your position", "ENTER":"ENTER", "BANK":'bank', "TO CALL":"Calls", "ACTION TO PLAYER":"player action now", "STATUS DECK ONE":"Shaffling the deck", "STATUS DECK TWO":"Ready", "TO FOLD":"Folds", "TO RAISE":"Raises", "TO RAISE ALL IN":"Raises all in!", "TO CHECK":"Checks", "TO BET":"bets", "POSITION":"Position", "MONEY":"Money","ALL END BYIN":"All end by in","PROFIT":"Profit"," Игроки получили свои карты ":"***Dealing down cards***"}
# Определили покерные комбинации

def info(info):
  if info == "info":
    for item in dictionary_of_combination:
      print(dictionary_of_combination[item])

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

## Функция парсинг ответа на предмет выбирания из него цифр
def parsing(answer):
  pars_answer = ""
  for item in answer:
    for i in range(10):
      if item == str(i):
        pars_answer = pars_answer + item
  if pars_answer == "":
    pars_answer = "1"
  return pars_answer
# Функция парсинг ответа на предмет выбирания из него цифр

import random 

# Перемешиваем колоду
def haos(deck):
  print(dictionary_of_message["STATUS DECK ONE"])
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
  print(dictionary_of_message["STATUS DECK TWO"])
  return deck_haos
# Колода перемешана


# Пристегните ремни, игра началась!!!

from datetime import datetime
import time

# Время
data = datetime.fromtimestamp(time.time()).strftime("%d.%m.%Y %H:%M:%S")

print(data)
#Время

# Welcome
print(dictionary_of_personal["NAME VLADELEC GAME"], Welcome["MESSAGE ONE"])
print(Welcome["MESSAGE TWO"])
# Welcome

# Игроки садятся за стол
print(Welcome["MESSAGE THREE"])
Players = []
n = 0
while not(n >= 2 and n <= 9):
  print("Введите количество игроков. От 2 до 9")
  n = input()
  n = parsing(n)
  n = int(n)
print("Введите имена игроков")
for i in range(n):
  Player = input()
  Players.append(Player)
# Players = []
# print("Введите имена игроков")
# n = 0
# while not(input() == ""):
#   n += 
#   Player = input()
#   Players.append(Player)

# Игроки сели, их имена лежат в Players
print(Welcome["MESSAGE FOUR"])

# Определяем баттон
k = 0
BUTTON = 0
while not(k == 1):
  k = 0
  print("Определяем баттон")
  deck = start_deck()
  deck_haos = haos(deck)
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
        cards_value[item] = power_cards["A"]
      if cards[item][0][0] == 'K':
        cards_value[item] = power_cards["K"]
      if cards[item][0][0] == 'Q':
        cards_value[item] = power_cards["Q"]
      if cards[item][0][0] == 'J':
        cards_value[item] = power_cards["J"]
      if cards[item][0][0] == 'T':
        cards_value[item] = power_cards["T"]
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
    position[Players_seat[0]] = [dictionary_of_position_HU["BUTTON, SMALL BLIND"]]
    position[Players_seat[1]] = [dictionary_of_position_6_max["BIG BLIND"]]
  if len(Players_seat) > 2:
    position[Players_seat[0]] = [dictionary_of_position_6_max["BUTTON"]]
    position[Players_seat[1]] = [dictionary_of_position_6_max["SMALL BLIND"]]
    position[Players_seat[2]] = [dictionary_of_position_6_max["BIG BLIND"]]
    if len(Players_seat) <= 6:
      if len(Players_seat) == 4:
        position[Players_seat[3]] = [dictionary_of_position_6_max["CATT OFF"]]
      if len(Players_seat) == 5:
        position[Players_seat[3]] = [dictionary_of_position_6_max["MIDDLE POSITION"]]
        position[Players_seat[4]] = [dictionary_of_position_6_max["CATT OFF"]]
      if len(Players_seat) == 6:
        position[Players_seat[3]] = [dictionary_of_position_6_max["EARLY POSITION"]]
        position[Players_seat[4]] = [dictionary_of_position_6_max["MIDDLE POSITION"]]
        position[Players_seat[5]] = [dictionary_of_position_6_max["CATT OFF"]]
    if (len(Players_seat) > 6) and (len(Players_seat) <= 9):
      if len(Players_seat) == 7:
        position[Players_seat[3]] = [dictionary_of_position_Full_Ring["UNDER THE GUN 1"]]
        position[Players_seat[4]] = [dictionary_of_position_Full_Ring["UNDER THE GUN 2"]]
        position[Players_seat[5]] = [dictionary_of_position_Full_Ring["UNDER THE GUN 3"]]
        position[Players_seat[6]] = [dictionary_of_position_Full_Ring["MIDDLE POSITION 1"]]
      if len(Players_seat) == 8:
        position[Players_seat[3]] = [dictionary_of_position_Full_Ring["UNDER THE GUN 1"]]
        position[Players_seat[4]] = [dictionary_of_position_Full_Ring["UNDER THE GUN 2"]]
        position[Players_seat[5]] = [dictionary_of_position_Full_Ring["UNDER THE GUN 3"]]
        position[Players_seat[6]] = [dictionary_of_position_Full_Ring["MIDDLE POSITION 1"]]
        position[Players_seat[7]] = [dictionary_of_position_Full_Ring["MIDDLE POSITION 2"]]
      if len(Players_seat) == 9:
        position[Players_seat[3]] = [dictionary_of_position_Full_Ring["UNDER THE GUN 1"]]
        position[Players_seat[4]] = [dictionary_of_position_Full_Ring["UNDER THE GUN 2"]]
        position[Players_seat[5]] = [dictionary_of_position_Full_Ring["UNDER THE GUN 3"]]
        position[Players_seat[6]] = [dictionary_of_position_Full_Ring["MIDDLE POSITION 1"]]
        position[Players_seat[7]] = [dictionary_of_position_Full_Ring["MIDDLE POSITION 2"]]
        position[Players_seat[8]] = [dictionary_of_position_Full_Ring["CATT OFF"]]
  return position
position = detected_position(Players_seat)
print(dictionary_of_message["POSITION"], position)
# Создали. Позиции игроков лежат в position
# Баттон определен. Места игроков за столом в Players_seat

# Закуп игроков

print(Welcome["MESSAGE FIVE"])

# Создаем словарь денег
money = {}
for item in Players_seat:
  money[item] = stack
print(dictionary_of_message["MONEY"], money)
# Создали. Количесто денег каждого игрока лежит в money

print(dictionary_of_message["ALL END BYIN"])

# Создаем словарь profit
profit = {}
for item in Players_seat:
  profit[item] = 0
print(dictionary_of_message["PROFIT"], profit)
# Создали. profit каждого игрока лежит в profit

# Все закупились

# Начало игры

status = dictionary_of_status["Go!"]

# Приветствие
print(Welcome["MESSAGE SIX"])
# Поприветствовали!

# Дисклеймер
print(Welcome["MESSAGE SEVEN"])
# Дисклеймер
game = 1
while not(status == dictionary_of_status["Stop!"]):
  print(dictionary_of_personal["DEALER"], "Game №", game)
# start and shaffling deck
  deck = start_deck()
  deck_haos = haos(deck)
# Перемешали

# Раздача карт

# Создаем пустой словарь
  cards = {}
# Создали

#Раздаем карты
  for item in Players_seat:
    cards[item] = [deck_haos[i], deck_haos[i+n]]
    i += 1
  print(cards)
  print(dictionary_of_message[" Игроки получили свои карты "])
  print(" Никому не показывайте свои карты, даже если человек представляется сотрудником Вашего Банка!")
# Карты ассоциированные с игроками лежат в cards

# Карты розданы. 

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

# Простановка блайндов  
  for item in Players_seat:
    if (position[item] == [dictionary_of_position_HU["BUTTON, SMALL BLIND"]]) or (position[item] == [dictionary_of_position_Full_Ring["SMALL BLIND"]]):
      money[item] = money[item] - small_blind
      bank = bank + small_blind
      action_blinds.append([item, position[item][0], dictionary_of_message["BET SMALL BLINDS"], small_blind])
      print(action_blinds)
      print(dictionary_of_personal["DEALER"], item, dictionary_of_message["BET SMALL BLINDS"], small_blind, USD["$"])
    if position[item] == [dictionary_of_position_Full_Ring["BIG BLIND"]]:
      money[item] = money[item] - big_blind
      bank = bank + big_blind
      action_blinds.append([item, position[item][0], dictionary_of_message["BET BIG BLINDS"], big_blind])
      print(action_blinds)
      print(dictionary_of_personal["DEALER"], item, dictionary_of_message["BET BIG BLINDS"], big_blind, USD["$"])
      print(money, dictionary_of_message["BANK"], bank)

# Ход игры
  
  print(action_blinds)
  print("***Dealing Preflop***")
  print(dictionary_of_message["POSITION"], position)

  while not(ishod == 1):
    k += 1
    for item in Players_seat:
      fold = folds_or_no(item, Players_folds)
      if fold == 0:
        to_call = last_raise - ( stack - money[item] )
        if to_call == 0:
          if position[item] == [dictionary_of_position_Full_Ring["BIG BLIND"]] and k == 0:
            pass
          if not(position[item] == [dictionary_of_position_Full_Ring["BIG BLIND"]] and k == 0):
            print(dictionary_of_personal["DEALER"], dictionary_of_message["BANK"], bank, USD["$"], dictionary_of_message["YOUR NONEY"], money[item], USD["$"], dictionary_of_message["YOUR POSITION"], position[item][0], dictionary_of_message["YOUR CARDS"], cards[item], item, dictionary_of_message["ENTER"], to_call, USD["$"], dictionary_of_action["TO CHECK"], dictionary_of_action["MIN"], big_blind, USD["$"], dictionary_of_action["TO BET"])
            answer = input()
            info(answer)
            answer = parsing(answer)
            answer = int(answer)
            if not((answer == 0) or ((answer >= big_blind) and (answer <= money[item]) and answer % big_blind == 0)):
              while not((answer == 0) or ((answer >= big_blind) and (answer <= money[item])and answer % big_blind == 0)):
                print(dictionary_of_personal["DEALER"], dictionary_of_message["BANK"], bank, USD["$"], dictionary_of_message["YOUR NONEY"], money[item], USD["$"], dictionary_of_message["YOUR POSITION"], position[item][0], dictionary_of_message["YOUR CARDS"], cards[item], item, dictionary_of_message["ENTER"], to_call, USD["$"], dictionary_of_action["TO CHECK"], dictionary_of_action["MIN"], big_blind, USD["$"],dictionary_of_action["TO BET"])
                answer = input()
                info(answer)
                answer = parsing(answer)
                answer = int(answer)
            if answer  == 0:
              action_preflop.append([item, position[item][0], dictionary_of_message["TO CHECK"]])
              print(action_preflop)
              print(dictionary_of_personal["DEALER"], item, position[item][0], dictionary_of_message["TO CHECK"])
            else:
              if position[item] == [dictionary_of_position_Full_Ring["BIG BLIND"]] and k == 1:
                money[item] = money[item] - answer + big_blind
              if (position[item] == [dictionary_of_position_Full_Ring["SMALL BLIND"]] or position[item] == [dictionary_of_position_HU["BUTTON, SMALL BLIND"]]) and k == 1:
                money[item] = money[item] - answer + small_blind
              if not((position[item] == [dictionary_of_position_Full_Ring["BIG BLIND"]] or position[item] == [dictionary_of_position_Full_Ring["SMALL BLIND"]] or position[item] == [dictionary_of_position_HU["BUTTON, SMALL BLIND"]]) and k == 1):
                for i in action_preflop:
                    if i == ["Preflop"]:
                      pass
                    else:
                      if i[0] == item and i[2] == "Raises":
                        last_raise_item_preflop = i[3]
                money[item] = money[item] - answer + last_raise_item_preflop
              bank = bank + answer
              if money[item] == 0:
                action_preflop.append([item, position[item][0], dictionary_of_message["TO BET"], answer])
                print(action_preflop)
                print(dictionary_of_personal["DEALER"], item, position[item][0], dictionary_of_message["TO BET ALL IN"], answer, USD["$"])
              else:
                action_preflop.append([item, position[item][0], dictionary_of_message["TO BET"], answer])
                print(action_preflop)
                print(dictionary_of_personal["DEALER"], item, position[item][0], dictionary_of_message["TO BET"], answer, USD["$"])
              last_raise = answer
        else:
          if (k == 0) and ((position[item] == [dictionary_of_position_HU["BUTTON, SMALL BLIND"]]) or (position[item] == [dictionary_of_position_6_max["SMALL BLIND"]]) or (position[item] == [dictionary_of_position_6_max["BUTTON"]])):
            pass
          else:
            print(dictionary_of_personal["DEALER"], dictionary_of_message["ACTION TO PLAYER"], item)
            print(dictionary_of_personal["DEALER"], dictionary_of_message["BANK"], bank, USD["$"], dictionary_of_message["YOUR NONEY"], money[item], USD["$"], dictionary_of_message["YOUR POSITION"], position[item][0],   dictionary_of_message["YOUR CARDS"], cards[item], item, dictionary_of_message["ENTER"], 0, dictionary_of_action["TO FOLD"],to_call, USD["$"], dictionary_of_action["TO CALL"], dictionary_of_action["MIN"], last_raise + big_blind, USD["$"], dictionary_of_action["TO RAISE"])
            answer = input()
            info(answer)
            answer = parsing(answer)
            answer = int(answer)
            if not((answer == 0) or (answer == to_call) or ((answer >= to_call * 2) and (answer <= money[item])and answer % big_blind == 0)):
              while not((answer == 0) or (answer == to_call) or ((answer >= to_call * 2) and (answer <= money[item])and answer % big_blind == 0)):
                print(dictionary_of_personal["DEALER"], dictionary_of_message["BANK"], bank, USD["$"], dictionary_of_message["YOUR NONEY"], money[item], USD["$"], dictionary_of_message["YOUR POSITION"], position[item][0], dictionary_of_message["YOUR CARDS"], cards[item], item, dictionary_of_message["ENTER"], 0,dictionary_of_action["TO FOLD"], to_call, USD["$"], dictionary_of_action["TO CALL"], dictionary_of_action["MIN"], last_raise + big_blind, USD["$"], dictionary_of_action["TO RAISE"])
                answer = input()
                info(answer)
                answer = parsing(answer)
                answer = int(answer)
            if answer == 0:
              action_preflop.append([item, position[item][0], dictionary_of_message["TO FOLD"]])
              Players_folds.append(item)
              print(action_preflop)
              print(dictionary_of_personal["DEALER"], item, position[item][0], dictionary_of_message["TO FOLD"])
            else:
              if answer == to_call:
                money[item] = money[item] - to_call
                bank = bank + to_call
                action_preflop.append([item, position[item][0], dictionary_of_message["TO CALL"], to_call])
                print(action_preflop)
                print(dictionary_of_personal["DEALER"], item, position[item][0], dictionary_of_message["TO CALL"], to_call, USD["$"])
              else:
                if (position[item] == [dictionary_of_position_Full_Ring["SMALL BLIND"]] or position[item] == [dictionary_of_position_HU["BUTTON, SMALL BLIND"]]) and k == 1:
                  money[item] = money[item] - answer + small_blind
                if position[item] == [dictionary_of_position_Full_Ring["BIG BLIND"]] and k == 1:
                  money[item] = money[item] - answer + big_blind
                if not(k == 1 and (position[item] == [dictionary_of_position_Full_Ring["SMALL BLIND"]] or position[item] == [dictionary_of_position_Full_Ring["BIG BLIND"]] or (position[item] == [dictionary_of_position_HU["BUTTON, SMALL BLIND"]]))):
                  for i in action_preflop:
                    if i == ["Preflop"]:
                      pass
                    else:
                      if i[0] == item and i[2] == "Raises":
                        last_raise_item_preflop = i[3]
                  money[item] = money[item] - answer + last_raise_item_preflop
                  bank = bank + answer
                if money[item] == 0:
                  action_preflop.append([item, position[item][0], dictionary_of_message["TO RAISE"], answer])
                  print(action_preflop)
                  print(dictionary_of_personal["DEALER"], item, position[item][0], dictionary_of_message["TO RAISE ALL IN"], answer, USD["$"])
                else:
                  action_preflop.append([item, position[item][0], dictionary_of_message["TO RAISE"], answer])
                  print(action_preflop)
                  print(dictionary_of_personal["DEALER"], item, position[item][0], dictionary_of_message["TO RAISE"], answer, USD["$"])
                last_raise = answer
      if who_is_her(Players_seat, Players_folds) == 1: break
      ishod = 1
      fold = 0
      item_copy = item
      for item in Players_seat:
        fold = folds_or_no(item, Players_folds)
        if fold == 0:
          if (stack - money[item]) > money_in_game:
            money_in_game = stack - money[item]
      for item in Players_seat:
        fold = folds_or_no(item, Players_folds)
        if fold == 0:
          if (stack - money[item]) == money_in_game:
            pass
          else:
            ishod += 1
      item = item_copy
      if k == 1 and last_raise == big_blind:
        if (ishod == 1):
          if position[item] == [dictionary_of_position_6_max["BIG BLIND"]]: break
      if k >= 1 and answer > big_blind:
        if (ishod == 1): break
      
  print(action_preflop)
# Блайнды проставлены
  print("***Dealing Flop***")
  print(dictionary_of_message["POSITION"], position)
  print(dictionary_of_personal["DEALER"], money, dictionary_of_message["BANK"], bank, USD["$"])

  flop = []
  for i in range(3):
    flop.append(deck_haos[2 * n + 1 + i])
  print(dictionary_of_personal["DEALER"], "Flop", flop)
  board = flop
  
  for item in Players_seat:
    fold = folds_or_no(item, Players_folds)
    if fold == 0:
      money_flop = money[item]
  action_flop = [["Flop"]] # Список действий префлоп
  to_call = -1 # Сумма, которую надо заколлировать игроку
  answer = 0 # Ответ игрока
  k = -1 # количество кругов торговли
  ishod = len(Players_seat)
  last_raise = 0
  money_in_game = 0
  last_raise_item_flop = 0
  
  if not(who_is_her(Players_seat, Players_folds) == 1) and not(money_in_game == stack):
    while not(ishod == 1 and k >= 1):
      k += 1
      for item in Players_seat:
        fold = folds_or_no(item, Players_folds)
        if fold == 0:
          to_call = last_raise - ( money_flop - money[item] )
          if to_call == 0:
            if position[item] == [dictionary_of_position_Full_Ring["BUTTON"]] and k == 0:
              pass
            else:
              print(dictionary_of_personal["DEALER"], dictionary_of_message["ACTION TO PLAYER"], item)
              print(dictionary_of_personal["DEALER"], dictionary_of_message["BANK"], bank, USD["$"], dictionary_of_message["YOUR NONEY"], money[item], USD["$"], dictionary_of_message["YOUR POSITION"], position[item][0], dictionary_of_message["YOUR CARDS"], cards[item], item, dictionary_of_message["ENTER"], to_call, USD["$"], dictionary_of_action["TO CHECK"], dictionary_of_action["MIN"], big_blind, USD["$"], dictionary_of_action["TO BET"])
              answer = input()
              info(answer)
              answer = parsing(answer)
              answer = int(answer)
              if not((answer == 0) or ((answer >= big_blind) and (answer <= money[item])and answer % big_blind == 0)):
                while not((answer == 0) or ((answer >= big_blind) and (answer <= money[item])and answer % big_blind == 0)):
                  print(dictionary_of_personal["DEALER"], dictionary_of_message["BANK"], bank, USD["$"], dictionary_of_message["YOUR NONEY"], money[item], USD["$"], dictionary_of_message["YOUR POSITION"], position[item][0], dictionary_of_message["YOUR CARDS"], cards[item], item, dictionary_of_message["ENTER"], to_call, USD["$"], dictionary_of_action["TO CHECK"], dictionary_of_action["MIN"], to_call * 2, USD["$"], dictionary_of_action["TO BET"])
                  answer = input()
                  info(answer)
                  answer = parsing(answer)
                  answer = int(answer)
              if answer == 0:
                action_flop.append([item, dictionary_of_message["TO CHECK"]])
                print(action_flop)
                print(dictionary_of_personal["DEALER"], item, position[item][0], dictionary_of_message["TO CHECK"])
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
                  action_flop.append([item, dictionary_of_message["TO BET"], answer])
                  print(action_flop)
                  print(dictionary_of_personal["DEALER"], item, position[item][0], dictionary_of_message["TO BET ALL IN"], answer, USD["$"])
                else:
                  action_flop.append([item, dictionary_of_message["TO BET"], answer])
                  print(action_flop)
                  print(dictionary_of_personal["DEALER"], item, position[item][0], dictionary_of_message["TO BET"], answer, USD["$"])
                last_raise = answer
          else:
            if (k == 0) and (position[item] == [dictionary_of_position_Full_Ring["BUTTON"]]):
              pass
            else:
              print(dictionary_of_personal["DEALER"], dictionary_of_message["ACTION TO PLAYER"], item)
              print(dictionary_of_personal["DEALER"], dictionary_of_message["BANK"], bank, USD["$"], dictionary_of_message["YOUR NONEY"], money[item], USD["$"], dictionary_of_message["YOUR POSITION"], position[item][0], dictionary_of_message["YOUR CARDS"], cards[item], item, dictionary_of_message["ENTER"], 0, dictionary_of_action["TO FOLD"], to_call, USD["$"], dictionary_of_action["TO CALL"], dictionary_of_action["MIN"], to_call + big_bling, USD["$"], dictionary_of_action["TO RAISE"])
              answer = input()
              info(answer)
              answer = parsing(answer)
              answer = int(answer)
              if not((answer == 0) or (answer == to_call) or ((answer >= to_call * 2) and (answer <= money[item])and answer % big_blind == 0)):
                while not((answer == 0) or (answer == to_call) or ((answer >= to_call * 2) and (answer <= money[item])and answer % big_blind == 0)):
                  print(dictionary_of_personal["DEALER"], dictionary_of_message["BANK"], bank, dictionary_of_message["YOUR NONEY"], money[item], dictionary_of_message["YOUR POSITION"], position[item][0], dictionary_of_message["YOUR CARDS"], cards[item], item, dictionary_of_message["ENTER"], 0, dictionary_of_action["TO FOLD"], to_call, dictionary_of_action["TO CALL"], dictionary_of_action["MIN"], to_call + big_bling, dictionary_of_action["TO RAISE"])
                  answer = input()
                  info(answer)
                  answer = parsing(answer)
                  answer = int(answer)
              if answer  == 0:
                action_flop.append([item, dictionary_of_message["TO FOLD"]])
                Players_folds.append(item)
                print(action_flop)
                print(dictionary_of_personal["DEALER"], item, position[item][0], dictionary_of_message["TO FOLD"])
              else:
                if answer == to_call:
                  money[item] = money[item] - to_call
                  bank = bank + to_call
                  action_flop.append([item, dictionary_of_message["TO CALL"], to_call])
                  print(action_flop)
                  print(dictionary_of_personal["DEALER"], item, position[item][0], dictionary_of_message["TO CALL"], to_call, USD["$"])
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
                    action_flop.append([item, position[item][0], dictionary_of_message["TO RAISE"], answer])
                    print(action_flop)
                    print(dictionary_of_personal["DEALER"], item, dictionary_of_message["TO RAISE ALL IN"], answer, USD["$"])
                  else:
                    action_flop.append([item, position[item][0], dictionary_of_message["TO RAISE"], answer])
                    print(action_flop)
                    print(dictionary_of_personal["DEALER"], item, position[item][0], dictionary_of_message["TO RAISE"], answer, USD["$"])
                  last_raise = answer
        ishod = 1
        fold = 0
        item_copy = item
        for item in Players_seat:
          fold = folds_or_no(item, Players_folds)
          if fold == 0:
            if (money_flop - money[item]) > money_in_game:
              money_in_game = money_flop - money[item]
        for item in Players_seat:
          fold = folds_or_no(item, Players_folds)
          if fold == 0:
            if (money_flop - money[item]) == money_in_game:
              pass
            else:
              ishod += 1
        item = item_copy
        if k == 1:
          if ishod == 1 and position[item] == [dictionary_of_position_6_max["BUTTON"]]: 
            break
        if k >= 2:
          if ishod == 1: break


  print(action_flop)
  print("***Dealing Turn***")
  print(dictionary_of_message["POSITION"], position)
  print(dictionary_of_personal["DEALER"], money, dictionary_of_message["BANK"], bank, USD["$"])

  turn = deck_haos[2 * n + 5 + i]
  board.append(turn)
  print(dictionary_of_personal["DEALER"], "Turn", board)

  for item in Players_seat:
    fold = folds_or_no(item, Players_folds)
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
  
  if not(who_is_her(Players_seat, Players_folds) == 1) and not(money_in_game == stack):
    while not(ishod == 1 and k >= 1):
      k += 1
      for item in Players_seat:
        fold = folds_or_no(item, Players_folds)
        if fold == 0:
          to_call = last_raise - ( money_turn - money[item] )
          if to_call == 0:
            if position[item] == [dictionary_of_position_Full_Ring["BUTTON"]] and k == 0:
              pass
            else:
              print(dictionary_of_personal["DEALER"], dictionary_of_message["ACTION TO PLAYER"], item)
              print(dictionary_of_personal["DEALER"], dictionary_of_message["BANK"], bank, USD["$"], dictionary_of_message["YOUR NONEY"], money[item], USD["$"], dictionary_of_message["YOUR POSITION"], position[item][0], dictionary_of_message["YOUR CARDS"], cards[item], item, dictionary_of_message["ENTER"], to_call, USD["$"], dictionary_of_action["TO CHECK"], dictionary_of_action["MIN"], big_blind, USD["$"], dictionary_of_action["TO BET"])
              answer = input()
              info(answer)
              answer = parsing(answer)
              answer = int(answer)
              if not((answer == 0) or ((answer >= big_blind) and (answer <= money[item])and answer % big_blind == 0)):
                while not((answer == 0) or ((answer >= big_blind) and (answer <= money[item])and answer % big_blind == 0)):
                  print(dictionary_of_personal["DEALER"], dictionary_of_message["BANK"], bank, dictionary_of_message["YOUR NONEY"], money[item], dictionary_of_message["YOUR POSITION"], position[item][0], dictionary_of_message["YOUR CARDS"], cards[item], item, dictionary_of_message["ENTER"], to_call, dictionary_of_action["TO CHECK"], dictionary_of_action["MIN"], to_call * 2, dictionary_of_action["TO BET"])
                  answer = input()
                  info(answer)
                  answer = parsing(answer)
                  answer = int(answer)
              if answer  == 0:
                action_turn.append([item, dictionary_of_message["TO CHECK"]])
                print(action_preflop)
                print(dictionary_of_personal["DEALER"], item, position[item][0], dictionary_of_message["TO CHECK"])
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
                  action_turn.append([item, dictionary_of_message["TO BET"], answer])
                  print(action_turn)
                  print(dictionary_of_personal["DEALER"], item, position[item][0], dictionary_of_message["TO RAISE ALL IN"], answer, USD["$"])
                else:
                  action_turn.append([item, dictionary_of_message["TO BET"], answer])
                  print(action_turn)
                  print(dictionary_of_personal["DEALER"], item, position[item][0], dictionary_of_message["TO BET"], answer, USD["$"])
                last_raise = answer
                last_raiser_turn = item 
          else:
            if (k == 0) and (position[item] == [dictionary_of_position_Full_Ring["BUTTON"]]):
              pass
            else:
              print(dictionary_of_personal["DEALER"], dictionary_of_message["ACTION TO PLAYER"], item)
              print(dictionary_of_personal["DEALER"], dictionary_of_message["BANK"], bank, USD["$"], dictionary_of_message["YOUR NONEY"], money[item], USD["$"], dictionary_of_message["YOUR POSITION"], position[item][0], dictionary_of_message["YOUR CARDS"], cards[item], item, dictionary_of_message["ENTER"], 0, dictionary_of_action["TO FOLD"], to_call, USD["$"], dictionary_of_action["TO CALL"], dictionary_of_action["MIN"], to_call + big_bling, USD["$"], dictionary_of_action["TO RAISE"])
              answer = input()
              info(answer)
              answer = parsing(answer)
              answer = int(answer)
              if not((answer == 0) or (answer == to_call) or ((answer >= to_call * 2) and (answer <= money[item])and answer % big_blind == 0)):
                while not((answer == 0) or (answer == to_call) or ((answer >= to_call * 2) and (answer <= money[item])and answer % big_blind == 0)):
                  print(dictionary_of_personal["DEALER"], dictionary_of_message["BANK"], bank, USD["$"], dictionary_of_message["YOUR NONEY"], money[item], USD["$"], dictionary_of_message["YOUR POSITION"], position[item][0], item, dictionary_of_message["ENTER"], 0, dictionary_of_action["TO FOLD"], to_call, USD["$"], dictionary_of_action["TO CALL"], dictionary_of_action["MIN"], to_call + big_bling, USD["$"], dictionary_of_action["TO RAISE"])
                  answer = input()
                  info(answer)
                  answer = parsing(answer)
                  answer = int(answer)
              if answer  == 0:
                action_turn.append([item, dictionary_of_message["TO FOLD"]])
                Players_folds.append(item)
                print(action_turn)
                print(dictionary_of_personal["DEALER"], item, position[item][0], dictionary_of_message["TO FOLD"])
              else:
                if answer == to_call:
                  money[item] = money[item] - to_call
                  bank = bank + to_call
                  action_turn.append([item, dictionary_of_message["TO CALL"], to_call])
                  print(dictionary_of_personal["DEALER"], item, position[item][0], dictionary_of_message["TO CALL"], to_call, USD["$"])
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
                    action_turn.append([item, position[item][0], dictionary_of_message["TO RAISE"], answer])
                    print(action_turn)
                    print(dictionary_of_personal["DEALER"], item, position[item][0], dictionary_of_message["TO RAISE ALL IN"], answer, USD["$"])
                  else:
                    action_turn.append([item, position[item][0], dictionary_of_message["TO RAISE"], answer])
                    print(action_turn)
                    print(dictionary_of_personal["DEALER"], item, position[item][0], dictionary_of_message["TO RAISE"], answer, USD["$"])
                  last_raise = answer
        ishod = 1
        fold = 0
        item_copy = item
        for item in Players_seat:
          fold = folds_or_no(item, Players_folds)
          if fold == 0:
            if (money_turn - money[item]) > money_in_game:
              money_in_game = money_turn - money[item]
        for item in Players_seat:
          fold = folds_or_no(item, Players_folds)
          if fold == 0:
            if (money_turn - money[item]) == money_in_game:
              pass
            else:
              ishod += 1
        item = item_copy
        if k == 1:
          if ishod == 1 and position[item] == [dictionary_of_position_6_max["BUTTON"]]: break
        if k >= 2:
          if ishod == 1: break

  print(action_turn)
  print("***Dealing River***")
  print(dictionary_of_message["POSITION"], position)
  print(dictionary_of_personal["DEALER"], money, dictionary_of_message["BANK"], bank, USD["$"])

  river = deck_haos[2 * n + 7 + i]
  board.append(river)
  print(dictionary_of_personal["DEALER"], "River", board)

  for item in Players_seat:
    fold = folds_or_no(item, Players_folds)
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
  
  if not(who_is_her(Players_seat, Players_folds) == 1) and not(money_in_game == stack):
    while not(ishod == 1 and k >= 1):
      k += 1
      for item in Players_seat:
        fold = folds_or_no(item, Players_folds)
        if fold == 0:
          to_call = last_raise - ( money_river - money[item] )
          if to_call == 0:
            if position[item] == [dictionary_of_position_Full_Ring["BUTTON"]] and k == 0:
              pass
            else:
              print(dictionary_of_personal["DEALER"], dictionary_of_message["ACTION TO PLAYER"], item)
              print(dictionary_of_personal["DEALER"], dictionary_of_message["BANK"], bank, USD["$"], dictionary_of_message["YOUR NONEY"], money[item], USD["$"], dictionary_of_message["YOUR POSITION"], position[item][0],dictionary_of_message["YOUR CARDS"], cards[item], item, dictionary_of_message["ENTER"], to_call, USD["$"], dictionary_of_action["TO CHECK"], dictionary_of_action["MIN"], big_blind, USD["$"], dictionary_of_action["TO BET"])
              answer = input()
              info(answer)
              answer = parsing(answer)
              answer = int(answer)
              if not((answer == 0) or ((answer >= big_blind) and (answer <= money[item])and answer % big_blind == 0)):
                while not((answer == 0) or ((answer >= big_blind) and (answer <= money[item])and answer % big_blind == 0)):
                  print(dictionary_of_personal["DEALER"], dictionary_of_message["BANK"], bank, USD["$"], dictionary_of_message["YOUR NONEY"], money[item], dictionary_of_message["YOUR POSITION"], position[item][0], dictionary_of_message["YOUR CARDS"], cards[item], item, dictionary_of_message["ENTER"], to_call, USD["$"], dictionary_of_action["TO CHECK"], dictionary_of_action["MIN"], to_call * 2, USD["$"], dictionary_of_action["TO BET"])
                  answer = input()
                  info(answer)
                  answer = parsing(answer)
                  answer = int(answer)
              if answer  == 0:
                action_river.append([item, dictionary_of_message["TO CHECK"]])
                print(action_preflop)
                print(dictionary_of_personal["DEALER"], item, position[item][0], dictionary_of_message["TO CHECK"])
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
                  action_river.append([item, dictionary_of_message["TO BET"], answer])
                  print(action_river)
                  print(dictionary_of_personal["DEALER"], item, position[item][0], dictionary_of_message["TO RAISE ALL IN"], answer, USD["$"])
                else:
                  action_river.append([item, dictionary_of_message["TO BET"], answer])
                  print(action_river)
                  print(dictionary_of_personal["DEALER"], item, position[item][0], dictionary_of_message["TO BET"], answer, USD["$"])
                last_raise = answer
          else:
            if (k == 0) and (position[item] == [dictionary_of_position_Full_Ring["BUTTON"]]):
              pass
            else:
              print(dictionary_of_personal["DEALER"], dictionary_of_message["ACTION TO PLAYER"], item)
              print(dictionary_of_personal["DEALER"], dictionary_of_message["BANK"], bank, USD["$"], dictionary_of_message["YOUR NONEY"], money[item], USD["$"], dictionary_of_message["YOUR POSITION"], position[item][0], dictionary_of_message["YOUR CARDS"], cards[item], item, dictionary_of_message["ENTER"], 0, dictionary_of_action["TO FOLD"], to_call, USD["$"], dictionary_of_action["TO CALL"], dictionary_of_action["MIN"], to_call + big_blind, USD["$"], dictionary_of_action["TO RAISE"])
              answer = input()
              info(answer)
              answer = parsing(answer)
              answer = int(answer)
              if not((answer == 0) or (answer == to_call) or ((answer >= to_call * 2) and (answer <= money[item])and answer % big_blind == 0)):
                while not((answer == 0) or (answer == to_call) or ((answer >= to_call * 2) and (answer <= money[item])and answer % big_blind == 0)):
                  print(dictionary_of_personal["DEALER"], dictionary_of_message["BANK"], bank, USD["$"], dictionary_of_message["YOUR NONEY"], money[item], USD["$"], dictionary_of_message["YOUR POSITION"], position[item][0], dictionary_of_message["YOUR CARDS"], cards[item], item, dictionary_of_message["ENTER"], 0, dictionary_of_action["TO FOLD"], to_call, USD["$"], dictionary_of_action["TO CALL"], dictionary_of_action["MIN"], to_call + big_blind, USD["$"], dictionary_of_action["TO RAISE"])
                  answer = input()
                  info(answer)
                  answer = parsing(answer)
                  answer = int(answer)
              if answer  == 0:
                action_river.append([item, dictionary_of_message["TO FOLD"]])
                Players_folds.append(item)
                print(action_river)
                print(dictionary_of_personal["DEALER"], item, position[item][0], dictionary_of_message["TO FOLD"])
              else:
                if answer == to_call:
                  money[item] = money[item] - to_call
                  bank = bank + to_call
                  action_river.append([item, dictionary_of_message["TO CALL"], to_call])
                  print(action_river)
                  print(dictionary_of_personal["DEALER"], item, position[item][0], dictionary_of_message["TO CALL"], to_call, USD["$"])
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
                    action_river.append([item, position[item][0], dictionary_of_message["TO RAISE"], answer])
                    print(action_river)
                    print(dictionary_of_personal["DEALER"], item, dictionary_of_message["TO RAISE ALL IN"], answer, USD["$"])
                  else:
                    action_river.append([item, position[item][0], dictionary_of_message["TO RAISE"], answer])
                    print(action_river)
                    print(dictionary_of_personal["DEALER"], item, dictionary_of_message["TO RAISE"], answer, USD["$"])
                  last_raise = answer
          ishod = 1
          fold = 0
          item_copy = item
          for item in Players_seat:
            fold = folds_or_no(item, Players_folds)
            if fold == 0:
              if (money_river - money[item]) > money_in_game:
                money_in_game = money_river - money[item]
          for item in Players_seat:
            fold = folds_or_no(item, Players_folds)
            if fold == 0:
              if (money_river - money[item]) == money_in_game:
                pass
              else:
                ishod += 1
          item = item_copy
          if k == 1:
            if ishod == 1 and position[item] == [dictionary_of_position_6_max["BUTTON"]]: break
          if k >= 2:
            if ishod == 1: break
  
  if who_is_her(Players_seat, Players_folds) > 1:
    print("***Show Down***")
    for item in Players_seat:
      fold = folds_or_no(item, Players_folds)
      if fold == 0:
        action_shows[item] = [dictionary_of_action["CARDS SHOWS"]]
        print(item, dictionary_of_action["CARDS SHOWS"], cards[item])
  
  print(action_river)
  print(dictionary_of_message["POSITION"], position)
  print(dictionary_of_personal["DEALER"], money, dictionary_of_message["BANK"], bank, USD["$"])
  
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