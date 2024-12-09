import PySimpleGUI as sg
from random import *
import webbrowser

sg.theme("DarkPurple3") # Устанавливаем тему для окна

text_size = 14 # размер шрифта
bot, human,сount = 0, 0, 0 # Счет бота, игрока и количество сыгранных раундов
# URL для рекламной ссылки
url = "https://1xlite-488389.top/ru?tag=s_3059277m_355c_151280&pb=50f0dbb198fc4ca08ad0a04a030fc2cf&click_id=674df308361e3900015f6607-12333&partner_id=151280"
# Списки изображений для различных ходов
demin_rock = ["demin_rock_reversed.png", "demin_rock.png"]
demin_scissors = ["demin_scissors_reversed.png", "demin_scissors.png"]
demin_paper = ["demin_paper_reversed.png", "demin_paper.png"]
image = ["rock.png","paper.png","scissors.png"]

# Функция для обновления счета в окне игры
def score_updater():
    window["user_score"].update(human) # Обновляем счет игрока
    window["bot_score"].update(bot) # Обновляем счет бота
# Основной макет игры
layout=[[sg.Text("Камень, ножницы и бумага, дааааааа",font=("Arial", text_size))],
        [sg.Text("Ваш ход, cчет: ",font=("Arial", text_size)), sg.Text(human, key="user_score", font=("Arial", text_size)), # счет игрока
         sg.Text("Ход противника, cчет: ",font=("Arial", text_size),size=(50,1),justification="right", ), sg.Text(bot, key="bot_score",
                font=("Arial", text_size))], #счет бота
        [sg.Image(filename='static.png', key="user_choice"),# Картинка выбора игрока
         sg.Image(filename='static.png', key="bot_choice")],# Картинка выбора бота
        [sg.Button("Камень",font=("Arial", text_size)),sg.Button("Ножницы",font=("Arial", text_size)),
                sg.Button("Бумага",font=("Arial", text_size))], # кнопки камень, ножницы, бумага
        [sg.Button("", image_filename="1xbet.png", image_size=(200, 80), key="add")]] #кнопка рекламы
# Макет для выбора противника и ввода данных игрока
layout2 = [[sg.Text("Выбери противника",font=("Arial", text_size))],[sg.Button("Жалкий кусок железяки",
                font=("Arial", text_size)),sg.Button("Потомственный маг",font=("Arial", text_size))], # выбор противника
           [sg.Text("Введите имя",font=("Arial", text_size)),sg.Push(),
            sg.Input(key="name_of_user",size=(20,1),font=("Arial", text_size))], # поле данных дл ввода имени
           [sg.Text("Введите количество раундов",font=("Arial", text_size)),
            sg.Input(key="count_matches",size=(20,1), font=("Arial", text_size))]] # поле данных для ввода количества раундов

choice_bot = sg.Window("Чей????",layout2)# Окно выбора противника
bot_move = choice(image) # Случайный ход бота

while 1:
    choice_of, values_of = choice_bot.read() # Чтение событий и значений из окна
    if choice_of == "Жалкий кусок железяки" or choice_of == "Потомственный маг" or choice_of == sg.WINDOW_CLOSED:
        if values_of["count_matches"] == "" or not(values_of["count_matches"].isdigit()): # Проверка ввода количества раундов
                sg.popup("Введите количество раундов", font=("Arial", text_size))# Предупреждение
        elif values_of["name_of_user"] == "" or values_of["name_of_user"].isdigit():# Проверка имени игрока
            sg.popup("Ну имя то введи", font=("Arial", text_size))# Предупреждение
        else:
            choice_bot.close()# Закрываем окно выбора
            break

window = sg.Window('ЧЕЙ?', layout)# Основное окно игры
while 1:
    event, values = window.read()# Чтение событий и значений

    if event == "add": # Переход по рекламе
        webbrowser.open(url)

    if choice_of == "Жалкий кусок железяки": # Логика для первого типа бота
        if event == "Камень":
            сount += 1  # Увеличиваем счетчик раундов
            bot_move = choice(image) # Случайный ход бота
            window["user_choice"].update(filename="rock.png") # Обновляем картинку выбора игрока
            window["bot_choice"].update(filename=image[image.index(bot_move)])# Обновляем картинку выбора бота
            if bot_move == "paper.png": # Логика выигрыша/проигрыша
                bot += 1
            elif bot_move == "scissors.png":
                human += 1
            score_updater()# Обновляем счет

        if event == "Бумага": # Аналогичная логика для кнопки "Бумага"
            сount += 1
            bot_move = choice(image)
            window["user_choice"].update(filename="paper.png")
            window["bot_choice"].update(filename=image[image.index(bot_move)])
            if bot_move == "scissors.png":
                bot += 1
            elif bot_move == "rock.png":
                human += 1
            score_updater()

        if event == "Ножницы": # Аналогичная логика для кнопки "Ножницы"
            сount += 1

            bot_move = choice(image)
            window["user_choice"].update(filename="scissors.png")
            window["bot_choice"].update(filename=image[image.index(bot_move)])
            if bot_move == "rock.png":
                bot += 1
            elif bot_move == "paper.png":
                human += 1
            score_updater()


    if choice_of == "Потомственный маг": # Логика для второго типа бота
        if event == "Камень":
            # Логика аналогична предыдущему боту, только здесь у игрока нет шанса выиграть
            window["user_choice"].update(filename="rock.png")
            window["bot_choice"].update(filename=choice(demin_paper))
            bot += 1
            сount += 1
            score_updater()
        elif event == "Бумага":
            window["user_choice"].update(filename="paper.png")
            window["bot_choice"].update(filename=choice(demin_scissors))
            bot += 1
            сount += 1
            score_updater()
        elif event == "Ножницы":
            window["user_choice"].update(filename="scissors.png")
            window["bot_choice"].update(filename=choice(demin_rock))
            bot += 1
            сount += 1
            score_updater()

    if event == sg.WINDOW_CLOSED or сount == int(values_of["count_matches"]):
        window.close() # Завершение игры
        layout3 = [[sg.Text(" ", font=("Arial", text_size), key="win_lose_noone")],
                   [sg.Image(key="win_lose_noone_image")]]
        result_window = sg.Window("ЙООУ", layout3,finalize=True, size=(600,600))# Окно с результатами игры
        if bot > human: # Логика определения победителя
            result_window["win_lose_noone"].update(f"вы проиграли!(( Счет: {human}:{bot}")
            result_window["win_lose_noone_image"].update(filename="demin_lose.png") #вывод счета и картинки, соответствующей результату игры
        elif bot < human:
            result_window["win_lose_noone"].update(f"Вы выиграли!)Счет: {human}:{bot}")
            result_window["win_lose_noone_image"].update(filename="demin_dab.png") #вывод счета и картинки, соответствующей результату игры
        else:
            result_window["win_lose_noone"].update(f"Ничья! Счет: {human}:{bot}")
            result_window["win_lose_noone_image"].update(filename="demin_3.png") #вывод счета и картинки, соответствующей результату игры
        while 1: # Ожидание закрытия окна результато
            event1, values = result_window.read()
            if event1 == sg.WINDOW_CLOSED:
                result_window.close()
                break
        break


with open('game_data.txt', 'a', encoding='utf-8') as file: # Запись результатов в файл
    file.write(f"{values_of['name_of_user']} {human}:{bot}\n")
file.close() # закрытие файла
