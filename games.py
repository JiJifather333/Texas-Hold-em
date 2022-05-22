from datetime import datetime
import time
import random

def declare_important_variables():
# Декларируются важные переменные для игры
  stack = 100000 # Закуп игроков. Используется в словаре money
  small_blind = stack // 200 # малый блайнд
  big_blind = stack // 100 # большой блайнд
  raik = 0.05 # переменная рейк этого казино
  return stack, small_blind, big_blind, raik

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

# Определяем словари
combination = {"Royal Flush":"Royal Flush  Ex.: As Ks Qs Js Ts","Street Flush":"Street Flush Ex.: Js Ts 9s 8s 7s","Kare":"Kare         Ex.: As Ad Ah At 2h","Full Haus":"Full Haus    Ex.: As Ad Ah Ks Kh","Flush":"Flush        Ex.: As Ks 7s 5s 2s","Street":"Street       Ex.: 9t 8s 7d 6h 5s", "Set":"Set          Ex.: As Ad Ah 4h 7s","Two Pair":"Two Pair     Ex.: As Ad Ks Kh 5t","Pair":"Pair         Ex.: As Ad Tt 6h 3d", "High card":"High Card    Ex.: Ks 9s 7d 4t 3h"}

nohand_combination = {"Street Draw":"Street Draw","Flush Draw":"Flush Draw", "Backdoor Street Draw":"Backdoor Street Draw", "Backdoor Flush":"Backdoor Flush", "Two OverCard":"Two OverCard", "One OverCard":"One OverCard","Nothing":"Nothing"}

position_HU = {"BUTTON, SMALL BLIND":"BTN, SB", "BIG BLIND":"BIG BLIND"}

action = {"MIN":"Минимум",  "TO FOLD":"Fold", "TO CALL":"Call", "TO RAISE":"Raise",  "TO CHECK":"Check", "TO BET":"Bet", "CARDS SHOWS":"Cards shows", "TO BET ALL IN":"TO bet all in"}

personal = {"NAME VLADELEC GAME": "NIKITA CHERNOV", "DEALER":"DEALER:"}
power_cards = {"A":13, "K":12, "Q":11, "J":10, "T":9, "7": 7, "6": 6, "5": 5, "4": 4, "3": 3, "2": 2}

position_6_max = {"EARLY POSITION":"EP","MIDDLE POSITION":"MP","CATT OFF":"CO","BUTTON":"BTN","SMALL BLIND":"SB","BIG BLIND":"BB"}

Welcome = {"MESSAGE ONE": " Добро пожаловать в самое прекрасное казино на свете CherCasino! CherCasino - деньги в корзину. Try your luck!", "MESSAGE TWO":"Стоп слово - Stop! Да да, не удивляйтесь", "MESSAGE THREE": " ++++ Игроки садятся за стол ++++", "MESSAGE FOUR":" ++++ Игроки сели за стол ++++", "MESSAGE FIVE":" by-in 100.000 $", "MESSAGE SIX":" Пристегните ремни, игра началась!!!", "MESSAGE SEVEN":" Если вы или ваши близкие страдают от игровой зависимости мы бы порекомендовали вам выйти из за стола. Но теперь каждый из вас покинет стол только если он пустой или мертвый. Удачи!"}

status_go = {"Go!": "Go!","Stop!":"Stop!"}

USD = {"$":"$"}
position_Full_Ring = {"UNDER THE GUN 1":"UTG 1", "UNDER THE GUN 2":"UTG 2", "UNDER THE GUN 3":"UTG 3", "MIDDLE POSITION 1":"MP 1", "MIDDLE POSITION 2":"MP 2", "CATT OFF":"CO", "BUTTON":"BTN","SMALL BLIND":"SB","BIG BLIND":"BB"}

message = {"YOUR CARDS": "your cards:","ENTER":"ENTER","BET SMALL BLINDS":"posts small blind","BET BIG BLINDS":"posts big blind" ,"YOUR NONEY":"Your money","YOUR POSITION":"Your position", "ENTER":"ENTER", "BANK":'bank', "TO CALL":"Calls", "ACTION TO PLAYER":"player action now", "STATUS DECK ONE":"Shaffling the deck", "STATUS DECK TWO":"Ready", "TO FOLD":"Folds", "TO RAISE":"Raises", "TO RAISE ALL IN":"Raises all in!", "TO CHECK":"Checks", "TO BET":"bets", "POSITION":"Position", "MONEY":"Money","ALL END BYIN":"All end by in","PROFIT":"Profit"," Игроки получили свои карты ":"***Dealing down cards***"}
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

# Перемешиваем колоду
def haos(deck):
  print(message["STATUS DECK ONE"])
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
  print(message["STATUS DECK TWO"])
  return deck_haos
# Колода перемешана

# Пристегните ремни, игра началась!!!

# Welcome
def welcome(personal, Welcome):
  print(personal["NAME VLADELEC GAME"], Welcome["MESSAGE ONE"])
  print(Welcome["MESSAGE TWO"])
# Welcome

# Игроки садятся за стол
def append_players(Welcome):
  print(Welcome["MESSAGE THREE"])
  Players = []
  n = 0
  while not(n >= 2 and n <= 9):
    print("Введите количество игроков. От 2 до 9")
    n = int(parsing(input()))
  print("Введите имена игроков")
  for i in range(n):
    Players.append(input())
  return n, Players


# Игроки сели, их имена лежат в Players
def message_four(Welcome):
  print(Welcome["MESSAGE FOUR"])

# Определяем баттон
def who_button(deck, power_cards, Players):
  k = 0
  BUTTON = 0 # Порядковый номер человека с наивысшей картой в списке Players
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
    high_value_cards = 0
    button = []
    cards_value = {}
    for item in cards:
      if (cards[item][0][0] == "A") or (cards[item][0][0] == "K") or (cards[item][0][0] == "Q") or (cards[item][0][0] == "J") or (cards[item][0][0] == "T"):
        if cards[item][0][0] == "A":
          cards_value[item] = power_cards["A"]
        if cards[item][0][0] == "K":
          cards_value[item] = power_cards["K"]
        if cards[item][0][0] == "Q":
          cards_value[item] = power_cards["Q"]
        if cards[item][0][0] == "J":
          cards_value[item] = power_cards["J"]
        if cards[item][0][0] == "T":
          cards_value[item] = power_cards["T"]
      else:
        cards_value[item] = int(cards[item][0][0])
    for item in cards_value:
      if cards_value[item] > high_value_cards:
        high_value_cards = cards_value[item]
        button = item
# Нужно, что проверить, что высшая карта одна, иначе раздать еще раз
    for item in cards_value:
      if cards_value[item] == high_value_cards:
        k += 1
    j = 0
    for item in Players:
      if item == button:
        BUTTON = j
      j += 1
  Players_seat = Players[BUTTON:] + Players[:BUTTON]
  return Players_seat

# Создаем словарь позиций
def detected_position(Players_seat):
  position = {}
  if len(Players_seat) == 2:
    position[Players_seat[0]] = [position_HU["BUTTON, SMALL BLIND"]]
    position[Players_seat[1]] = [position_6_max["BIG BLIND"]]
  if len(Players_seat) > 2:
    position[Players_seat[0]] = [position_6_max["BUTTON"]]
    position[Players_seat[1]] = [position_6_max["SMALL BLIND"]]
    position[Players_seat[2]] = [position_6_max["BIG BLIND"]]
    if len(Players_seat) <= 6:
      if len(Players_seat) == 4:
        position[Players_seat[3]] = [position_6_max["CATT OFF"]]
      if len(Players_seat) == 5:
        position[Players_seat[3]] = [position_6_max["MIDDLE POSITION"]]
        position[Players_seat[4]] = [position_6_max["CATT OFF"]]
      if len(Players_seat) == 6:
        position[Players_seat[3]] = [position_6_max["EARLY POSITION"]]
        position[Players_seat[4]] = [position_6_max["MIDDLE POSITION"]]
        position[Players_seat[5]] = [position_6_max["CATT OFF"]]
    if (len(Players_seat) > 6) and (len(Players_seat) <= 9):
      if len(Players_seat) == 7:
        position[Players_seat[3]] = [position_Full_Ring["UNDER THE GUN 1"]]
        position[Players_seat[4]] = [position_Full_Ring["UNDER THE GUN 2"]]
        position[Players_seat[5]] = [position_Full_Ring["UNDER THE GUN 3"]]
        position[Players_seat[6]] = [position_Full_Ring["MIDDLE POSITION 1"]]
      if len(Players_seat) == 8:
        position[Players_seat[3]] = [position_Full_Ring["UNDER THE GUN 1"]]
        position[Players_seat[4]] = [position_Full_Ring["UNDER THE GUN 2"]]
        position[Players_seat[5]] = [position_Full_Ring["UNDER THE GUN 3"]]
        position[Players_seat[6]] = [position_Full_Ring["MIDDLE POSITION 1"]]
        position[Players_seat[7]] = [position_Full_Ring["MIDDLE POSITION 2"]]
      if len(Players_seat) == 9:
        position[Players_seat[3]] = [position_Full_Ring["UNDER THE GUN 1"]]
        position[Players_seat[4]] = [position_Full_Ring["UNDER THE GUN 2"]]
        position[Players_seat[5]] = [position_Full_Ring["UNDER THE GUN 3"]]
        position[Players_seat[6]] = [position_Full_Ring["MIDDLE POSITION 1"]]
        position[Players_seat[7]] = [position_Full_Ring["MIDDLE POSITION 2"]]
        position[Players_seat[8]] = [position_Full_Ring["CATT OFF"]]
  return position

# Закуп игроков
def message_five(Welcome):
  print(Welcome["MESSAGE FIVE"])

# Создаем словарь денег
def money(Players_seat, stack, message):
  money = {}
  for item in Players_seat:
    money[item] = stack
  print(message["MONEY"], money)
  print(message["ALL END BYIN"])
  return money

# Начало игры ####################################################??????????????????
#Очень неопределенное место. Когда игра должна страртовать? Будет
#много игр, и параллелльно. Надо их нумеровать. Будет несколько процессов.
def start_game(status_go, Welcome):
  status = status_go["Go!"]
  print(Welcome["MESSAGE SIX"])
  print(Welcome["MESSAGE SEVEN"])
  number_game = 1
  return status, number_game
###################################################################

#Далее пойдет сама функция game!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def game(status_go, personal, number_game, Players_seat, n, message, position, position_HU, position_6_max, position_Full_Ring, USD, stack, big_blind, small_blind):

  while not(status == status_go["Stop!"]):

    print(personal["DEALER"], "Game №", number_game)

    def cards_down_night(Players_seat, n):
# start and shaffling deck
      deck = start_deck()
      deck_haos = haos(deck)
      cards = {}
      for item in Players_seat:
        i = 0
        cards[item] = [deck_haos[i], deck_haos[i + n]]
        i += 1
      print(message[" Игроки получили свои карты "])
      print("Никому не показывайте ваши карты, даже если человек представляется сотрудником Вашего Банка!")
      return cards

    cards = cards_down_night(Players_seat,n)
  
# Карты розданы. 

    bank = 0 # Переменная банк
    action_blinds = [["Blinds"]] # Список дейстий блайнды
    action_preflop = [["Preflop"]] # Список действий префлоп
    Players_folds = [] # Список сфолдивших игроков
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
      if (position[item] == [position_HU["BUTTON, SMALL BLIND"]]) or (position[item] == [position_Full_Ring["SMALL BLIND"]]):
        money[item] = money[item] - small_blind
        bank = bank + small_blind
        action_blinds.append([item, position[item][0], message["BET SMALL BLINDS"], small_blind])
        print(action_blinds)
        print(personal["DEALER"], item, message["BET SMALL BLINDS"], small_blind, USD["$"])
      if position[item] == [position_Full_Ring["BIG BLIND"]]:
        money[item] = money[item] - big_blind
        bank = bank + big_blind
        action_blinds.append([item, position[item][0], message["BET BIG BLINDS"], big_blind])
        print(action_blinds)
        print(personal["DEALER"], item, message["BET BIG BLINDS"], big_blind, USD["$"])
        print(money, message["BANK"], bank)

# Ход игры
  
    print(action_blinds)
    print("***Dealing Preflop***")
    print(message["POSITION"], position)
####################################################################################################Delete
    def get_answer_to_check(personal, message, bank, USD, money, position, cards, item, to_call, action, answer, big_blind):
      print(personal["DEALER"], message["BANK"], bank, USD["$"], message["YOUR NONEY"], money[item], USD["$"], message["YOUR POSITION"], position[item][0], message["YOUR CARDS"], cards[item], item, message["ENTER"], to_call, USD["$"], action["TO CHECK"], action["MIN"], big_blind, USD["$"], action["TO BET"])
      answer = input()
      info(answer)
      answer = parsing(answer)
      answer = int(answer)
      if not((answer == 0) or ((answer >= big_blind) and (answer <= money[item]) and answer % big_blind == 0)):
        while not((answer == 0) or ((answer >= big_blind) and (answer <= money[item])and answer % big_blind == 0)):
          print(personal["DEALER"], message["BANK"], bank, USD["$"], message["YOUR NONEY"], money[item], USD["$"], message["YOUR POSITION"], position[item][0], message["YOUR CARDS"], cards[item], item, message["ENTER"], to_call, USD["$"], action["TO CHECK"], action["MIN"], big_blind, USD["$"], action["TO BET"])
          answer = input()
          info(answer)
          answer = int(parsing(answer))
      return answer

    def analis_answer_after_check_bet_preflop(answer, action_preflop, item, position, message, personal, position_Full_Ring, k, money, big_blind, position_HU, last_raise_item_preflop, bank, last_raise):
      if answer  == 0:
        action_preflop.append([item, position[item][0], message["TO CHECK"]])
        print(action_preflop)
        print(personal["DEALER"], item, position[item][0], message["TO CHECK"])
      else:
        if position[item] == [position_Full_Ring["BIG BLIND"]] and k == 1:
          money[item] = money[item] - answer + big_blind
        if (position[item] == [position_Full_Ring["SMALL BLIND"]] or position[item] == [position_HU["BUTTON, SMALL BLIND"]]) and k == 1:
          money[item] = money[item] - answer + small_blind
        if not((position[item] == [position_Full_Ring["BIG BLIND"]] or position[item] == [position_Full_Ring["SMALL BLIND"]] or position[item] == [position_HU["BUTTON, SMALL BLIND"]]) and k == 1):
          for i in action_preflop:
            if i == ["Preflop"]:
              pass
            else:
              if i[0] == item and i[2] == "Raises":
                last_raise_item_preflop = i[3]
          money[item] = money[item] - answer + last_raise_item_preflop
        bank = bank + answer
        if money[item] == 0:
          action_preflop.append([item, position[item][0], message["TO BET"], answer])
          print(action_preflop)
          print(personal["DEALER"], item, position[item][0], message["TO BET ALL IN"], answer, USD["$"])
        else:
          action_preflop.append([item, position[item][0], message["TO BET"], answer])
          print(action_preflop)
          print(personal["DEALER"], item, position[item][0], message["TO BET"], answer, USD["$"])
        last_raise = answer
      return action_preflop, money, bank, last_raise_item_preflop, last_raise
######################################################################################################Delete
    def get_answer_to_call_raise(personal, message, item, bank, USD, money, position, cards, action, to_call, last_raise, big_blind, answer):
      print(personal["DEALER"], message["ACTION TO PLAYER"], item)
      print(personal["DEALER"], message["BANK"], bank, USD["$"], message["YOUR NONEY"], money[item], USD["$"], message["YOUR POSITION"], position[item][0], message["YOUR CARDS"], cards[item], item, message["ENTER"], 0, action["TO FOLD"], to_call, USD["$"], action["TO CALL"], action["MIN"], last_raise + big_blind, USD["$"], action["TO RAISE"])
      answer = input()
      info(answer)
      answer = int(parsing(answer))
      if not((answer == 0) or (answer == to_call) or ((answer >= to_call + big_blind) and (answer <= money[item])and answer % big_blind == 0)):
        while not((answer == 0) or (answer == to_call) or ((answer >= to_call + big_blind) and (answer <= money[item])and answer % big_blind == 0)):
          print(personal["DEALER"], message["BANK"], bank, USD["$"], message["YOUR NONEY"], money[item], USD["$"], message["YOUR POSITION"], position[item][0], message["YOUR CARDS"], cards[item], item, message["ENTER"], 0, action["TO FOLD"], to_call, USD["$"], action["TO CALL"], action["MIN"], last_raise + big_blind, USD["$"], action["TO RAISE"])
          answer = input()
          info(answer)
          answer = int(parsing(answer))
      return answer

    def analis_answer_after_call_raise_preflop(answer, k, money, to_call, bank, action_preflop, personal, position, message, item, USD, Players_folds, position_Full_Ring, position_HU, last_raise_item_preflop, last_raise):
      if answer == 0:
        action_preflop.append([item, position[item][0], message["TO FOLD"]])
        Players_folds.append(item)
        print(action_preflop)
        print(personal["DEALER"], item, position[item][0], message["TO FOLD"])
      else:
        if answer == to_call:
          money[item] = money[item] - to_call
          bank = bank + to_call
          action_preflop.append([item, position[item][0], message["TO CALL"], to_call])
          print(action_preflop)
          print(personal["DEALER"], item, position[item][0], message["TO CALL"], to_call, USD["$"])
        else:
          if (position[item] == [position_Full_Ring["SMALL BLIND"]] or position[item] == [position_HU["BUTTON, SMALL BLIND"]]) and k == 1:
            money[item] = money[item] - answer + small_blind
          if position[item] == [position_Full_Ring["BIG BLIND"]] and k == 1:
            money[item] = money[item] - answer + big_blind
          if not(k == 1 and (position[item] == [position_Full_Ring["SMALL BLIND"]] or position[item] == [position_Full_Ring["BIG BLIND"]] or (position[item] == [position_HU["BUTTON, SMALL BLIND"]]))):
            for i in action_preflop:
              if i == ["Preflop"]:
                pass
              else:
                if i[0] == item and i[2] == "Raises":
                  last_raise_item_preflop = i[3]
            money[item] = money[item] - answer + last_raise_item_preflop
          bank = bank + answer
          if money[item] == 0:
            action_preflop.append([item, position[item][0], message["TO RAISE"], answer])
            print(action_preflop)
            print(personal["DEALER"], item, position[item][0], message["TO RAISE ALL IN"], answer, USD["$"])
          else:
            action_preflop.append([item, position[item][0], message["TO RAISE"], answer])
            print(action_preflop)
            print(personal["DEALER"], item, position[item][0], message["TO RAISE"], answer, USD["$"])
          last_raise = answer
      return action_preflop, Players_folds, money, last_raise_item_preflop, bank, last_raise
##############################################################################################
    while not(ishod == 1):
      k += 1
      for item in Players_seat:
        if len(Players_folds) == len(Players_seat) - 1: break
        fold = folds_or_no(item, Players_folds)
        if fold == 0:
          to_call = last_raise - ( stack - money[item] )
          for i in action_preflop:
            if i == ["Preflop"]:
              pass
            else:
              if i[0] == item and i[2] == "Raises":
                last_raise_item_preflop = i[3]
          if to_call == 0 and not(k > 1 and last_raise == last_raise_item_preflop):
            if position[item] == [position_Full_Ring["BIG BLIND"]] and k == 0:
              pass
          else:
            if (k == 0) and ((position[item] == [position_HU["BUTTON, SMALL BLIND"]]) or (position[item] == [position_6_max["SMALL BLIND"]]) or (position[item] == [position_6_max["BUTTON"]])):
              pass
            if last_raise == last_raise_item_preflop:
              pass
            else:
              answer = get_answer_to_call_raise(personal, message, item, bank, USD, money, position, cards, action, to_call, last_raise, big_blind, answer)
              action_preflop, Players_folds, money, last_raise_item_preflop, bank, last_raise = analis_answer_after_call_raise_preflop(answer, k, money, to_call, bank, action_preflop, personal, position, message, item, USD, Players_folds, position_Full_Ring, position_HU, last_raise_item_preflop, last_raise)
        if who_is_her(Players_seat, Players_folds) == 1: break
        ishod = 1
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
   ############################################################################## дальше флоп   
    print(action_preflop)
# Блайнды проставлены
    print("***Dealing Flop***")
    print(message["POSITION"], position)
    print(personal["DEALER"], money, message["BANK"], bank, USD["$"])

    def analis_answer_after_check_bet_flop(answer, action_flop, message, personal, position, item, last_raise_item_flop, money, bank, USD, last_raise):
      if answer == 0:
        action_flop.append([item, message["TO CHECK"]])
        print(action_flop)
        print(personal["DEALER"], item, position[item][0], message["TO CHECK"])
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
          action_flop.append([item, message["TO BET"], answer])
          print(action_flop)
          print(personal["DEALER"], item, position[item][0], message["TO BET ALL IN"], answer, USD["$"])
        else:
          action_flop.append([item, message["TO BET"], answer])
          print(action_flop)
          print(personal["DEALER"], item, position[item][0], message["TO BET"], answer, USD["$"])
        last_raise = answer
      return action_flop, last_raise_item_flop, money, bank, last_raise

    def analis_answer_after_call_raise_flop(answer, action_flop, item, message, Players_folds, position, to_call, money, bank, USD, last_raise_item_flop, last_raise):
      if answer  == 0:
        action_flop.append([item, message["TO FOLD"]])
        Players_folds.append(item)
        print(action_flop)
        print(personal["DEALER"], item, position[item][0], message["TO FOLD"])
      else:
        if answer == to_call:
          money[item] = money[item] - to_call
          bank = bank + to_call
          action_flop.append([item, message["TO CALL"], to_call])
          print(action_flop)
          print(personal["DEALER"], item, position[item][0], message["TO CALL"], to_call, USD["$"])
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
            action_flop.append([item, position[item][0], message["TO RAISE"], answer])
            print(action_flop)
            print(personal["DEALER"], item, message["TO RAISE ALL IN"], answer, USD["$"])
          else:
            action_flop.append([item, position[item][0], message["TO RAISE"], answer])
            print(action_flop)
            print(personal["DEALER"], item, position[item][0], message["TO RAISE"], answer, USD["$"])
          last_raise = answer
        return action_flop, Players_folds, money, bank, last_raise_item_flop, last_raise

    flop = []
    for i in range(3):
      flop.append(deck_haos[2 * n + 1 + i])
    print(personal["DEALER"], "Flop", flop)
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
          if len(Players_folds) == len(Players_seat) - 1: break
          fold = folds_or_no(item, Players_folds)
          if fold == 0:
            to_call = last_raise - ( money_flop - money[item] )
            for i in action_preflop:
              if i == ["Flop"]:
                pass
              else:
                if i[0] == item and i[2] == "Raises":
                  last_raise_item_preflop = i[3]
            if to_call == 0 and not(k > 1 and last_raise == last_raise_item_reflop):
              if position[item] == [dictionary_of_position_Full_Ring["BUTTON"]] and k == 0:
                pass
              else:
                answer = get_answer_to_check(personal, message, bank, USD, money, position, cards, item, to_call, action, answer, big_blind)
                action_flop, last_raise_item_flop, money, bank, last_raise = analis_answer_after_check_bet_flop(answer, action_flop, message, personal, position, item, last_raise_item_flop, money, bank, USD, last_raise)
            else:
              if (k == 0) and (position[item] == [dictionary_of_position_Full_Ring["BUTTON"]]):
                pass
              else:
                answer = get_answer_to_call_raise(personal, message, item, bank, USD, money, position, cards, action, to_call, last_raise, big_blind, answer)             
                action_flop, Players_folds, money, bank, last_raise_item_flop, last_raise = analis_answer_after_call_raise_flop(answer, action_flop, item, message, Players_folds, position, to_call, money, bank, USD, last_raise_item_flop, last_raise)
          if who_is_her(Players_seat, Players_folds) == 1: break
          ishod = 1
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


    print(action_flop)
    print("***Dealing Turn***")
    print(message["POSITION"], position)
    print(personal["DEALER"], money, message["BANK"], bank, USD["$"])

    def analis_answer_after_check_bet_turn(answer, action_turn, message, personal, position, item, last_raise_item_fturn, money, bank, USD, last_raise):
      if answer == 0:
        action_turn.append([item, message["TO CHECK"]])
        print(action_turn)
        print(personal["DEALER"], item, position[item][0], message["TO CHECK"])
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
          action_turn.append([item, message["TO BET"], answer])
          print(action_turn)
          print(personal["DEALER"], item, position[item][0], message["TO BET ALL IN"], answer, USD["$"])
        else:
          action_turn.append([item, message["TO BET"], answer])
          print(action_turn)
          print(personal["DEALER"], item, position[item][0], message["TO BET"], answer, USD["$"])
        last_raise = answer
      return action_turn, last_raise_item_turn, money, bank, last_raise

    def analis_answer_after_call_raise_turn(answer, action_flop, item, message, Players_folds, position, to_call, money, bank, USD, last_raise_item_flop, last_raise):
      if answer  == 0:
        action_turn.append([item, message["TO FOLD"]])
        Players_folds.append(item)
        print(action_turn)
        print(personal["DEALER"], item, position[item][0], message["TO FOLD"])
      else:
        if answer == to_call:
          money[item] = money[item] - to_call
          bank = bank + to_call
          action_turn.append([item, message["TO CALL"], to_call])
          print(action_turn)
          print(personal["DEALER"], item, position[item][0], message["TO CALL"], to_call, USD["$"])
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
            action_turn.append([item, position[item][0], message["TO RAISE"], answer])
            print(action_turn)
            print(personal["DEALER"], item, message["TO RAISE ALL IN"], answer, USD["$"])
          else:
            action_turn.append([item, position[item][0], message["TO RAISE"], answer])
            print(action_turn)
            print(personal["DEALER"], item, position[item][0], message["TO RAISE"], answer, USD["$"])
          last_raise = answer
        return action_turn, Players_folds, money, bank, last_raise_item_turn, last_raise

    turn = deck_haos[2 * n + 5 + 1]
    board.append(turn)
    print(personal["DEALER"], "Turn", board)

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
          if len(Players_folds) == len(Players_seat) - 1: break
          fold = folds_or_no(item, Players_folds)
          if fold == 0:
            to_call = last_raise - ( money_turn - money[item] )
            for i in action_preflop:
              if i == ["Preflop"]:
                pass
              else:
                if i[0] == item and i[2] == "Raises":
                  last_raise_item_preflop = i[3]
            if to_call == 0 and not(k > 1 and last_raise == last_raise_item_reflop):
              if position[item] == [dictionary_of_position_Full_Ring["BUTTON"]] and k == 0:
                pass
              else:
                answer = get_answer_to_check(personal, message, bank, USD, money, position, cards, item, to_call, action, answer, big_blind)
                action_turn, last_raise_item_turn, money, bank, last_raise = analis_answer_after_check_bet_turn(answer, action_turn, message, personal, position, item, last_raise_item_fturn, money, bank, USD, last_raise)
            else:
              if (k == 0) and (position[item] == [dictionary_of_position_Full_Ring["BUTTON"]]):
                pass
              else:
                answer = get_answer_to_call_raise(personal, message, item, bank, USD, money, position, cards, action, to_call, last_raise, big_blind, answer)
                action_turn, Players_folds, money, bank, last_raise_item_turn, last_raise = analis_answer_after_call_raise_turn(answer, action_flop, item, message, Players_folds, position, to_call, money, bank, USD, last_raise_item_flop, last_raise)
          if who_is_her(Players_seat, Players_folds) == 1: break
          ishod = 1
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

    print(action_turn)
    print("***Dealing River***")
    print(message["POSITION"], position)
    print(personal["DEALER"], money, message["BANK"], bank, USD["$"])

    def analis_answer_after_check_bet_river(answer, action_turn, message, personal, position, item, last_raise_item_fturn, money, bank, USD, last_raise):
      if answer == 0:
        action_river.append([item, message["TO CHECK"]])
        print(action_river)
        print(personal["DEALER"], item, position[item][0], message["TO CHECK"])
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
          action_river.append([item, message["TO BET"], answer])
          print(action_river)
          print(personal["DEALER"], item, position[item][0], message["TO BET ALL IN"], answer, USD["$"])
        else:
          action_river.append([item, message["TO BET"], answer])
          print(action_river)
          print(personal["DEALER"], item, position[item][0], message["TO BET"], answer, USD["$"])
        last_raise = answer
      return action_river, last_raise_item_river, money, bank, last_raise

    def analis_answer_after_call_raise_river(answer, action_flop, item, message, Players_folds, position, to_call, money, bank, USD, last_raise_item_flop, last_raise):
      if answer  == 0:
        action_turn.append([item, message["TO FOLD"]])
        Players_folds.append(item)
        print(action_turn)
        print(personal["DEALER"], item, position[item][0], message["TO FOLD"])
      else:
        if answer == to_call:
          money[item] = money[item] - to_call
          bank = bank + to_call
          action_turn.append([item, message["TO CALL"], to_call])
          print(action_river)
          print(personal["DEALER"], item, position[item][0], message["TO CALL"], to_call, USD["$"])
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
            action_river.append([item, position[item][0], message["TO RAISE"], answer])
            print(action_river)
            print(personal["DEALER"], item, message["TO RAISE ALL IN"], answer, USD["$"])
          else:
            action_river.append([item, position[item][0], message["TO RAISE"], answer])
            print(action_river)
            print(personal["DEALER"], item, position[item][0], message["TO RAISE"], answer, USD["$"])
          last_raise = answer
        return action_river, Players_folds, money, bank, last_raise_item_river, last_raise

    river = deck_haos[2 * n + 7 + 1]
    board.append(river)
    print(personal["DEALER"], "River", board)

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
          if len(Players_folds) == len(Players_seat) - 1: break
          fold = folds_or_no(item, Players_folds)
          if fold == 0:
            to_call = last_raise - ( money_river - money[item] )
            for i in action_preflop:
              if i == ["Preflop"]:
                pass
              else:
                if i[0] == item and i[2] == "Raises":
                  last_raise_item_preflop = i[3]
            if to_call == 0 and not(k > 1 and last_raise == last_raise_item_reflop):
              if position[item] == [dictionary_of_position_Full_Ring["BUTTON"]] and k == 0:
                pass
              else:
                answer = get_answer_to_check(personal, message, bank, USD, money, position, cards, item, to_call, action, answer, big_blind)
                action_river, last_raise_item_river, money, bank, last_raise = analis_answer_after_check_bet_river(answer, action_turn, message, personal, position, item, last_raise_item_fturn, money, bank, USD, last_raise)
            else:
              if (k == 0) and (position[item] == [dictionary_of_position_Full_Ring["BUTTON"]]):
                pass
              else:
                answer = get_answer_to_call_raise(personal, message, item, bank, USD, money, position, cards, action, to_call, last_raise, big_blind, answer)
                action_river, Players_folds, money, bank, last_raise_item_river, last_raise = analis_answer_after_call_raise_river(answer, action_flop, item, message, Players_folds, position, to_call, money, bank, USD, last_raise_item_flop, last_raise)
            if who_is_her(Players_seat, Players_folds) == 1: break
            ishod = 1
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
    number_game += 1
    Players_seat = Players[0:] + Players[:0]
    position = detected_position(Players_seat)
    for item in Players_seat:
      money[item] = stack
# Сброс   

    status = input()
