'''# 1
words=input().split()
for i in range(len(words)-1):
    if words[i] != words[i+1]:
        print(words[i],end = " ")
print(words[-1])
'''
'''# 2
print(' '.join(input().split()[::-1]))
'''
'''# 3
def f(a):
    return '.'.join(a)
print(f(input()))
'''
'''# 4
a = input()
if 'не плохо' in a:
    print(a.replace("не плохо","хорошо"))
'''
"""#5
def f(a):
    alf,c='уеыаоэюияёУЕЫАОЭЮИЯЁ',0
    for i in range(len(a)):
        if a[i] in alf:
            c+=1
    return c
a=input()
b=a.split('/')
if len(b)==3:
    a1,a2,a3=b[0],b[1],b[2]
    if f(a1) == 5 and f(a3) == 5 and f(a2) == 7:
        print("ХАЙКУ!!!")
    else:
        print("Не хайку :(")
else:
    print('должно быть 3 строки')
"""
'''#6
word,new_word,new_word_1=input(),"",""
if word[-1]=="#":
    word=word[:-1]
    for i in range(len(word)):
        if i % 2 == 0:
            new_word+=word[i]
        else:
            new_word_1= word[i]+new_word_1
else:
    print("отсутствует знак #")
print(new_word+new_word_1)
'''
'''#7
import random
length,up=int(input("Желаемая длинa пароля (целое число): ")),input("нужны ли заглавные буквы (да/нет): ")
low,dig=input("нужны ли строчные буквы (да/нет): "),input("нужны ли цифры (да/нет): ")
spec=input("нужны ли специальные символы (да/нет): ")
alf_up,alf_low,alf_spec="QWERTYUIOPLKJMHNGBFVDCSXAZ","qwertyuioplkjmhngbfvdcsxaz",";:?,.<>`~[]{}|/-=+)(*&^%$#@!"
password=""
for i in range(length):
    if up == "да":
        password += random.choice(alf_up)
    if low == "да":
        password += random.choice(alf_low)
    if dig == "да":
        password += str(random.randint(0,9))
    if spec == "да":
        password += random.choice(alf_spec)
    if len(password) >= length:
        password=password[:length]
        print(password)
        break
'''
#8
scoreboard=input()
def f(a):
    return a.split()
def team(a):
    return a.split("-")
def score(a):
    return a.split(":")
teams=team(f(scoreboard)[0])
scores=score(f(scoreboard)[1])
if int(scores[0])>int(scores[1]):
    print(teams[0])
elif int(scores[0])<int(scores[1]):
    print(teams[1])
else:
    print("Ничья")
