#практикум
'''

#1
#print(int(input())*70+int(input())*140)

#2
temp=int(input())
print(temp*1.8+32,temp+273.15)

#3
month_num=int(input())
if month_num <=2 or month_num == 12:
    print('winter')
elif month_num<=5:
    print('spring')
elif month_num<=11:
    print('autumn')
else:
    print('error')

#laba

#1

#print(int(input())*86400+int(input())*3600+int(input())*60+int(input()))

#2
#print(int(input())%(10**int(input())))

#3
num=input()
array=[]
for i in range(len(num)):
    array.append(int(num[i]))
print(sum(array))
'''
#4
#choice = int(input('''Вы находитесь в землях, заселенных драконами. Перед собой вы
#видите две пещеры. В одной из них — дружелюбный дракон, который готов поделиться с
#вами своими сокровищами.
#Во второй — жадный и голодный дракон, который мигом вас съест.
#В какую пещеру вы войдете? (нажмите клавишу 1 или 2)\n'''))
#print('''Вы приближаетесь к пещере...
#Ее темнота заставляет вас дрожать от страха...
#Большой дракон выпрыгивает перед вами! Он раскрывает свою
#пасть и''')
'''
if choice == 1:
    print('...делится с вами своими сокровищами!
')
elif choice == 2:
    print(' ...моментально вас съедает!')
else:
    print('error')
    
#5
a,b,c=int(input()),int(input()),int(input())
if a==b and b==c:
    print('правильный')
elif a!=b and b!=c and a!=c:
    print('разносторонний')
elif a==b and a!=c or a==c and a!=b or b==c and c!=a:
    print('равнобедренный')
else:
    print('error')
    
#6
month=input()
if month == 'январь' or month == 'март' or month == 'май' or\
   month == 'июль' or month == 'август' or month == 'октябрь' or\
   month == 'декабрь':
    print('31')
elif month=='февраль':
    print('28 или 29')
else:
    print('30')


#7
'''
car_num = input()
alf='QWERTYUIOPLKJHGFDSAZXCVBNM'
dig='1234567890'
if len(car_num)==6:
    if car_num[0] in alf and car_num[1] in alf and car_num[2] in alf and\
       car_num[3] in dig and car_num[4] in dig and car_num[5] in dig:
        print('Старый')
elif len(car_num)==7:
    if car_num[0] in dig and car_num[1] in dig and car_num[2] in dig and\
       car_num[3] in dig and car_num[4] in alf and car_num[5] in alf and\
       car_num[6] in alf:
        print('Новый')
else:
    print('error')




