import dictionary
import function
import games

#Определение важных переменных
function.famous_variable()

#ИНИЦИАЛИЗАЦИЯ ИГРЫ------------------------------------------------------

# Пристегните ремни, игра началась!!!

# Время
function.g_time()
#Время

# Welcome
function.welcome()
# Welcome

# Игроки садятся за стол
Players = function.players_seat()

function.message_four()

# Определяем баттон
Players_seat = function.detected_button(Players)

# Создаем словарь позиций
position = detected_position(Players_seat)
# Создали. Позиции игроков лежат в position
# Баттон определен. Места игроков за столом в Players_seat

# Закуп игроков

function.message_five()

# Создаем словарь денег
money = function.money(Players_seat)
# Создали. Количесто денег каждого игрока лежит в money

function.by()

# Создаем словарь profit
profit = function.profit(Players_seat)
# Создали. profit каждого игрока лежит в profit
#ИНИЦИАЛИЗАЦИЯ ИГРЫ------------------------------------------------------
# Все закупились

# Начало игры

games.game(Players_seat, position, money, profit, n, stack, small_blind, big_blind)

status = dictionary.status["Go!"]


