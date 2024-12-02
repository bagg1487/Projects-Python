import PySimpleGUI as sg
from random import *
sg.theme("DarkPurple3")
text_size = 14
bot,human=0,0
image_demin=["demin_static.png","demin_rock.gif","demin_paper.gif","demin_scirrors.gif"]
image=['static.png',"rock.gif","paper.gif","scirrors.gif"]
images = ["demin_5.png", "demin_2.png", "demin_3.png","demin_4.png"]
layout=[[sg.Text("Камень, ножницы и бумага, дааааааа"),sg.Text(f"{bot}:{human}",key="score")],
        [sg.Text("Введите количество раундов"),sg.Input(key="count_matches",size=(20,1))],
        [sg.Image(key="demin"),sg.Image(key="kbn")],
        [sg.Button("Камень"),sg.Button("Ножницы"),sg.Button("Бумага")]]
layout2 = [[sg.Text("Выбери противника")],[sg.Button("Жалкий кусок железяки"),sg.Button("Потомственный маг")]]
choice_bot = sg.Window("Чей????",layout2)
while 1:
    choice_of, values_of = choice_bot.read()
    print(choice_of, values_of)
    if choice_of == sg.WINDOW_CLOSED:
        break
    if choice_of == "Жалкий кусок железяки" or choice_of == "Потомственный маг":
        choice_bot.close()
        window = sg.Window('ЧЕЙ?', layout)
        while 1:
            event, values = window.read()
            window["kbn"].update(filename=images[0])
            if choice_of == "Потомственный маг":
                window["demin"].update(filename=images[0])
                if event == "Камень":
                    bot_xod = randint(1, 3)
                    window["kbn"].update(filename=images[1])
                    window["demin"].update(filename=images[bot_xod])
                    if bot_xod == 2:
                        bot += 1
                    elif bot_xod == 3:
                        human += 1
                elif event == "Бумага":
                    window["kbn"].update(filename=images[2])
                    window["demin"].update(filename=images[3])
                    if bot_xod == 3:
                        bot += 1
                    elif bot_xod == 1:
                        human += 1
                elif event == "Ножницы":
                    window["kbn"].update(filename=images[3])
                    window["demin"].update(filename=images[1])
                    if bot_xod == 1:
                        bot += 1
                    elif bot_xod == 3:
                        human += 1
            if choice_of == "Потомственный маг":
                window["demin"].update(filename=images[1])
                if event == "Камень":
                    window["kbn"].update(filename=images[1])
                    window["demin"].update(filename=images[2])
                    bot += 1
                elif event == "Бумага":
                    window["kbn"].update(filename=images[2])
                    window["demin"].update(filename=images[3])
                    bot += 1
                elif event == "Ножницы":
                    window["kbn"].update(filename=images[3])
                    window["demin"].update(filename=images[1])
                    bot += 1
            if event == sg.WINDOW_CLOSED or bot+human == window["count_matches"]:
                if bot > human:
                    sg.popup("вы проиграли!((")
                elif bot < human:
                    sg.popup("Вы выиграли!)")
                else:
                    sg.popup("Ничья!")
                break
        window.close()