#1
# array,alf,dig = [1,32,'qa','asd','qw',3,'z'],[],[]
# for i in range(len(array)):
#     dig.append(array[i]) if isinstance(array[i],int) else alf.append(array[i])
# print(alf,dig)
#2
# import random
# array=[]
# while len(array)<6:
#     array.append(random.randint(1,49))
# print(array)
#3
# list,array=[1,3,45,789,0,-2,7020,-345678],[]
# for i in range(len(list)-1):
#     if list[i]<list[i+1]:
#         array.append(list[i+1])
# print(array)
#4
# nums,dig,sum,low,max = input(),[],0,[],[]
# dig.append(nums)
# while nums != '':
#     nums = input()
#     if nums != "":
#         dig.append(nums)
# for i in range(len(dig)):
#     sum+=int(dig[i])
#     ave=sum/len(dig)
#     if int(dig[i])<int(ave):
#         low.append(dig[i])
#     else:
#         max.append(dig[i])
# print(ave,low,max)
#5
# rost,rost1,a = [215, 207, 196, 176, 168, 166],int(input()),[]
# for i in range(len(rost)):
#     if rost1<=rost[i]:
#         a.append(i+2)
# print(max(a))
#6
# import random
# a,count,combo=[],0,0
# while combo != 1:
#     count+=1
#     orel_reshka = random.choice(["O","P"])
#     a.append(orel_reshka)
#     for i in range(len(a)-2):
#         if a[i]==a[i+1]==a[i+2]:
#             combo+=1
#             print(a,count)
#             break
#7
# card,sum_even,sum_odd=input(),0,0
# for i in range(len(card)):
#     if i % 2 != 0:
#         sum_even+=int(card[i])
#
#     else:
#         if (int(card[i])*2)<=9:
#             sum_odd+=int(card[i])*2
#         else:
#             sum_odd += int(card[i])*2-9
# if (sum_odd+sum_even)%10==0:
#     print('correctly')
# else:
#     print("uncorrectly")
#8
# count,words=int(input()),[]
# while count>0:
#     word=input()
#     if len(word)<=10:
#         words.append(word)
#     else:
#         words.append(word[0]+str(len(word)-2)+word[-1])
#     count-=1
# for i in range(len(words)):
#     print(words[i])
#9
# n,count=int(input()),0
# while n!=0:
#     a=input().split()
#     if a[0]<a[1]:
#         count+=1
#     n-=1
# print(count)

