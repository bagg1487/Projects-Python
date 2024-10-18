#Лабораторная работа
#задание 1
'''
height=int(input())
array=[]
array.append(height)
if height==0:
    print('error')
while height != 0:
    height=int(input())
    if height > 0 and height != 0:
        array.append(height)
    elif height < 0:
        print('error')
if len(array)<2:
    print('error')
else:
    print('max height: ',max(array),'min height: ',(min(array)))
'''
#задание 2
'''
num,summa=int(input()),0
for i in range(2,101,2):
    summa+=i
if summa==num:
    print('correct')
else:
    print('uncorrect')
'''
#задание 3
'''
n,i,a=int(input()),1,0
while i<n+1:
    a+=i**2
    i+=1
print(a)
'''
#задание 4
'''
n,b=int(input()),-1
for i in range(n,0,-1):
    b+=2
    print(" "*i,"#"*b)
print(" "*n,"#")      
'''
#задание 5
'''
dog_age=int(input())
if dog_age>0:
    if 1<=dog_age<=2:
        print('age = 10.5')
    else:
        print('age = 24')
else:
    print('error')
'''
#задание 6
'''
import random


print("Хорошо, я загадал число. Попробуй его отгадать")

def f():
    secret,count = random.randint(1, 10),0
    while 1:
        count+=1
        print(count, 'попытка: ')
        num = int(input())
        if num > secret:
            print('Меньше')
        elif num < secret:
            print('Больше')
        elif num == secret:
            print("Поздравляю! Вы угадали!Количество попыток: ", count)
            break
        else:
            print("Нее, ты не угадал. Попробуй снова")
f()
if input("Хотите продолжить игру? Да, Нет: ") == 'Да':
    f()
elif input("Хотите продолжить игру? Да, Нет: ") == 'Нет':
    print('Конец!')
else:
    print('error')
'''
'''
#задание 7
bilet=input()
if len(bilet)==6:
    if int(bilet[0])+int(bilet[1])+int(bilet[2])==int(bilet[3])\
       +int(bilet[4])+int(bilet[5]):
        print('Lucky')
    else:
        print('Unlucky')
else:
    print('error')
'''
#задание 8
a=input()
print(int(a,2))
