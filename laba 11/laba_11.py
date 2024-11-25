#1
# keyboard_symbols = {'1':'.,!?:','2': "ABC", '3': "DEF", '4': "GHI",
#                     '5': "JKL",'6': "MNO", '7': "PQRS", '8': "TUV", '9': "WXYZ", '0': ' '}
# string = input().upper()
# for symbol in string:
#     for button_number in keyboard_symbols:
#         if symbol in keyboard_symbols[button_number]:
#             for symbol_position in keyboard_symbols[button_number]:
#                 if symbol_position == symbol:
#                     print(button_number, end='')
#                     break
#                 else:
#                     print(button_number, end='')
#             print(" ", end='')
#2
# score = {'1': "AEILNORSTU", '2': 'DG','3': 'BCMP', '4': 'FHVWY', '5': 'K', '8': 'JX', '10': 'QZ'}
# string = input().upper()
# final_score = 0
# for symbol in string:
#     for points in score:
#         if symbol in score[points]:
#             final_score += int(points)
# print(final_score)
#3
# emails = {'gryffindor.com': ['andrei_serov', 'alexander_pushkin', 'elena_belova', 'k_stepanov'],
# 'hufflepuff.com': ['alena.semyonova', 'ivan.polekhin', 'marina_abrabova'],
# 'hogwarts.com': ['sergei.zharkov', 'julia_lyubimova', 'vitaliy.smirnoff'],
# 'slytherin.com': ['ekaterina_ivanova', 'glebova_nastya'],
# 'ravenclaw.com': ['john.doe', 'mark.zuckerberg', 'helen_hunt']}
# index_of_names_list = 0
# first_part_mail = list(emails.values())
# second_part_mail = list(emails.keys())
# for names_list in first_part_mail:
#     for i in range(len(names_list)):
#         print(f'{names_list[i]}@{second_part_mail[index_of_names_list]} ',end=' ')
#     print()
#     index_of_names_list += 1
#4
# from random import *
# import PySimpleGUI as sg
# sg.theme("DarkBrown")
# sg.theme_previewer()
# text_size=17
# layout = [[sg.Text("Введите границы для рандома:",font=("Arial", text_size))],
#     [sg.Text("Нижняя граница",font=("Arial", text_size), size=(20, 1)), sg.InputText(key="low", font=("Arial", text_size),size=(10, 1))],
#     [sg.Text("Верхняя граница",font=("Arial", text_size), size=(20, 1)), sg.InputText(key="up", font=("Arial", text_size),size=(10, 1))],
#     [sg.Button("Сгенерировать",font=("Arial", 16), size=(15, 1))],
#     [sg.Text("Рейтинг равен:",font=("Arial", text_size)), sg.Text("", font=("Arial", text_size), key="Output")],
#     [sg.Image(key="IMAGE")],]
# window = sg.Window("Калькулятор рейтинга по физике", layout)
# while 1:
#     event, values = window.read()
#     if event == "Сгенерировать":
#         low = int(values["low"])
#         up = int(values["up"])
#         if low > up:
#             sg.popup_error("первое значение больше",font=("Arial", text_size))
#         window["Output"].update(randint(low, up))
#         window["IMAGE"].update(filename="example_1.png")
#     elif event == sg.WINDOW_CLOSED:
#         break
# window.close()
#5
# import PySimpleGUI as sg
# sg.theme("DarkPurple4")
# text_size = 17
# layout = [[sg.Text("Добро пожаловать в игру \"Эрудит\" от самого сильного мага\n всея СибГУТИ Сергея Демина. Дерзайте ввести свое слово! ",font=("Arial", text_size)),sg.InputText(key="word",font=("Arial", text_size),size=(20,2))],
#           [sg.Image(filename="example_3.png")],
#           [sg.Button("Посчитать сумму о4ков",font=("Arial", text_size),size=(20,1))],
#           [sg.Text("Сумма очков равна:",font=("Arial", text_size)),(sg.Text("",font=("Arial", text_size), key="Output"))]]
# window = sg.Window("ЧЕЙ?", layout,size=(1000,1000))
# while 1:
#      event, values = window.read()
#      score = {'1': "AEILNORSTU", '2': 'DG', '3': 'BCMP', '4': 'FHVWY', '5': 'K', '8': 'JX', '10': 'QZ'}
#      string = str(values["word"]).upper()
#      final_score = 0
#      for symbol in string:
#           for points in score:
#                if symbol in score[points]:
#                     final_score += int(points)
#      if event == "Посчитать сумму о4ков":
#           window["Output"].update(final_score)
#      elif event == sg.WINDOW_CLOSED:
#           break
# window.close()

