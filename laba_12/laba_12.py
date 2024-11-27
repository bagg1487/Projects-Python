 #1
# people_dict={"1_priority": [],"2_priority": [],'3_priority': []}
# for i in range(int(input("Количество людей: "))):
#     people = input(f"{i+1} человек: ").split()
#     if people[-1] == "man":
#         people_dict["2_priority"].append(people[0])
#     elif people[-1] == "woman" or people[-1] == "child":
#         people_dict["1_priority"].append(people[0])
#     elif people[-1] == "captain":
#         people_dict["3_priority"].append(people[0])
# print(*people_dict["1_priority"], *people_dict["2_priority"], *people_dict["3_priority"])
#2
# messages_count,message=int(input("Количество сообщений:")),input("Сообщение:").upper()
# if len(message) == messages_count:
#     if message.count("Q") == message.count("A") and message[-1] != "Q":
#         print("+")
#     else:
#         print("-")
# else:
#     print("длина не совпадает")
#3
# import PySimpleGUI as sg
# from random import *
# c_image = [[sg.Image("bio.png")]]
# c_input = [[sg.Text("Введите количество бактерий:", font="Arial 20"), sg.Input(font="Arial 20", size=(5, 0), key="micro")],
#            [sg.Text("Количество секунд:", font="Arial 20"), sg.Input(font="Arial 20", size=(5, 0), key="count")],
#            [sg.Text("Количество делений:", font="Arial 20"), sg.Input(font="Arial 20", size=(5, 0), key="division")],
#            [sg.Text("Результат:", font="Arial 20"), sg.Input(font="Arial 20", readonly=True, size=(5, 0), key="res")],
#            [sg.Button("Рассчитать", font="Arial 20")]]
#
# layout = [[sg.Column(c_image), sg.VSeperator(), sg.Column(c_input, justification='right')]]
# window = sg.Window("Калькулятор бактерий", layout)
# while 1:
#     event, value = window.read()
#     if event == sg.WIN_CLOSED:
#         break
#     micro = int(value["micro"])  #здесь хранится количество бактерий изначально
#     count = int(value["count"])  #здесь хранится количество секунд для которых требуется рассчитать
#     division = int(value["division"])
#     res = 0                 #здесь будет храниться результат
#     #код надо писать здесь
#     if event == "Рассчитать":
#         for i in range(count):
#             res += division * micro + randint(0,4)
#         window["res"].update(res)
# window.close()
#4
#import PySimpleGUI as sg
#from time import *
# def binary_num():
#     return "\n".join([bin(integer)[2:].zfill(8) for integer in range(1, 128)])
# def inverse(binary):
#     binary = binary.replace("0", "*")
#     binary = binary.replace("1", "0")
#     binary = binary.replace("*", "1")
#     return ''.join(binary)
# def additional(inverse):
#     inter = inverse.split("\n")
#     arr = [bin(int(num, 2) + 1)[2:] for num in inter]
#     return '\n'.join(arr)
#
# sg.theme("DarkPurple3")
# text_size=17
# #images = ["demin_5.png", "demin_2.png", "demin_3.png","demin_4.png"]
# images = ["nenado_0.png","nenado_1.png"]
# layout = [[sg.Text("Привет, вы снова в игре от Сергея Демина. Тут нада тыкать кнопачки",font=("Arial", text_size))],
#           [sg.Image(key="demin",size=(520,520))],
#           [sg.Button("Прямой код",font=("Arial", text_size),size=(20,1)), sg.Button("Обратный код",font=("Arial", text_size),size=(20,1)),sg.Button("Дополнительный код",font=("Arial", text_size),size=(20,1))],
#           [sg.Multiline('',font=("Arial", text_size), background_color="#222222", size = (40, 20), disabled=True, autoscroll=True,key="Output")]]
# window = sg.Window("ЧЕЙ?", layout,size=(1000,1000))
# current_index = 0
# last_time = time()
# while 1:
#     event,values = window.read(timeout=100)
#     if time() - last_time >= 1:
#         current_index = (current_index + 1) % len(images)
#         window["demin"].update(filename=images[current_index],size=(520,520))
#         last_time = time()
#     if event == "Прямой код":
#         window["Output"].update(binary_num())
#     elif event == "Обратный код":
#         window["Output"].update(inverse(binary_num()))
#     elif event == "Дополнительный код":
#         window["Output"].update(additional(inverse(binary_num())))
#     if event == sg.WINDOW_CLOSED:
#               break
# window.close()



