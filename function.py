import dictionary

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
# Колода перемешана
