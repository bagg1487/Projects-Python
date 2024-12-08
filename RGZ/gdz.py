import PySimpleGUI as sg
from random import *
import webbrowser

sg.theme("DarkPurple3")

text_size = 14
bot, human,сount = 0, 0, 0

url = "https://1xlite-488389.top/ru?tag=s_3059277m_355c_151280&pb=50f0dbb198fc4ca08ad0a04a030fc2cf&click_id=674df308361e3900015f6607-12333&partner_id=151280"
demin_rock = ["demin_rock_reversed.png", "demin_rock.png"]
demin_scissors = ["demin_scissors_reversed.png", "demin_scissors.png"]
demin_paper = ["demin_paper_reversed.png", "demin_paper.png"]
image = ["rock.png","paper.png","scissors.png"]

def score_updater():
    window["user_score"].update(human)
    window["bot_score"].update(bot)
layout=[[sg.Text("Камень, ножницы и бумага, дааааааа",font=("Arial", text_size))],
        [sg.Text("Ваш ход, cчет: ",font=("Arial", text_size)), sg.Text(human, key="user_score", font=("Arial", text_size)),sg.Text("Ход противника, cчет: ",font=("Arial", text_size),size=(50,1),justification="right", ), sg.Text(bot, key="bot_score",
                font=("Arial", text_size))],
        [sg.Image(filename='static.png', key="user_choice"),sg.Image(filename='static.png', key="bot_choice")],
        [sg.Button("Камень",font=("Arial", text_size)),sg.Button("Ножницы",font=("Arial", text_size)),
                sg.Button("Бумага",font=("Arial", text_size))],
        [sg.Button("", image_filename="1xbet.png", image_size=(200, 80), key="add")]]

layout2 = [[sg.Text("Выбери противника",font=("Arial", text_size))],[sg.Button("Жалкий кусок железяки",
                font=("Arial", text_size)),sg.Button("Потомственный маг",font=("Arial", text_size))],
           [sg.Text("Введите имя",font=("Arial", text_size)),sg.Push(),sg.Input(key="name_of_user",size=(20,1),font=("Arial", text_size))],
           [sg.Text("Введите количество раундов",font=("Arial", text_size)),sg.Input(key="count_matches",size=(20,1), font=("Arial", text_size))]]

choice_bot = sg.Window("Чей????",layout2)
bot_move = choice(image)

while 1:
    choice_of, values_of = choice_bot.read()
    if choice_of == "Жалкий кусок железяки" or choice_of == "Потомственный маг" or choice_of == sg.WINDOW_CLOSED:
        if values_of["count_matches"] == "" or not(values_of["count_matches"].isdigit()):
                sg.popup("Введите количество раундов", font=("Arial", text_size))
        elif values_of["name_of_user"] == "" or values_of["name_of_user"].isdigit():
            sg.popup("Ну имя то введи", font=("Arial", text_size))
        else:
            choice_bot.close()
            break

window = sg.Window('ЧЕЙ?', layout)
while 1:
    event, values = window.read()

    if event == "add":
        webbrowser.open(url)

    if choice_of == "Жалкий кусок железяки":

        if event == "Камень":
            сount += 1
            bot_move = choice(image)
            window["user_choice"].update(filename="rock.png")
            window["bot_choice"].update(filename=image[image.index(bot_move)])
            if bot_move == "paper.png":
                bot += 1
            elif bot_move == "scissors.png":
                human += 1
            score_updater()

        if event == "Бумага":
            сount += 1
            bot_move = choice(image)
            window["user_choice"].update(filename="paper.png")
            window["bot_choice"].update(filename=image[image.index(bot_move)])
            if bot_move == "scissors.png":
                bot += 1
            elif bot_move == "rock.png":
                human += 1
            score_updater()

        if event == "Ножницы":
            сount += 1

            bot_move = choice(image)
            window["user_choice"].update(filename="scissors.png")
            window["bot_choice"].update(filename=image[image.index(bot_move)])
            if bot_move == "rock.png":
                bot += 1
            elif bot_move == "paper.png":
                human += 1
            score_updater()


    if choice_of == "Потомственный маг":
        if event == "Камень":
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
        window.close()
        if bot > human:
            sg.popup(f"вы проиграли!(( Счет: {human}:{bot}",font=("Arial", text_size))
        elif bot < human:
            sg.popup(f"Вы выиграли!)Счет: {human}:{bot}",font=("Arial", text_size))
        else:
            sg.popup(f"Ничья! Счет: {human}:{bot}",font=("Arial", text_size))
        break

with open('game_data.txt', 'a', encoding='utf-8') as file:
    file.write(f"{values_of["name_of_user"]} {human}:{bot}\n")
file.close()
