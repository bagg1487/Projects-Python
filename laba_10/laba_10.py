#1
# text,score= open("file4.txt",encoding="UTF8").readlines(),[]
# for word in text:
#     human=word.split()
#     score.append(human[-1])
# score[score.index(max(score))]="0"
# print(text[score.index(max(score))])
#2
# file5,file6=open("file5.txt",encoding="UTF8").readlines(),open("file6.txt",encoding="UTF8").readlines()
# for i in file5:
#     if "Academy" in i:
#         print("file5")
#         break
# for i in file6:
#     if "Academy" in file6:
#         print("file6")
#         break
#3
# file6=open("file6.txt",encoding="UTF8").readlines()
# count_common,count_e=0,0
# for words in file6:
#     words.split()
#     for i in range(len(words)):
#         count_common+=len(words[i])
#         if "." in words[i] or "," in words[i]:
#             count_common-=1
#         if "e" in words[i]:
#             count_e+=1
# print(f"Количество букв е: {round((count_e/count_common)*100,2)}")
#4
# file7,file8=open("file7.txt",encoding="UTF8").readlines(),open("file8.txt",encoding="UTF8").readlines()
# n,gender,count=int(input()),input(),0
# if gender == "man":
#     for i in file8:
#         print(i.split()[0])
#         count+=1
#         if count==n:
#             break
# else:
#     for i in file7:
#         print(i.split()[0])
#         count += 1
#         if count == n:
#             break
#5
# file_99=open("file_99.txt").readlines()
# new_word=input()
# length_text,sum_word,index_last_word=0,0,0
# for i in file_99:
#     word=i.split()
#     for f in word:
#         length_text+=len(f)
# for f in word:
#     sum_word += len(f)
#     index_last_word+=1
#     if sum_word >= length_text//2:
#         print(sum_word)
#         print(index_last_word)
#         break
# for i in range(len(word)):
#     if i<index_last_word:
#         print(word[i],end=" ")
#     elif i==index_last_word:
#         print(new_word, word[i],end=" ")
#     else:
#         print(word[i],end=" ")
#6
# file_990=open("file_990.txt").readlines()
# for word in file_990:
#     words=word.split()
#     for j in words:
#         reverse=''.join(reversed(j))
#         print(reverse,end=" ")
#7
# from  random import *
# file0=open("file0.txt").readlines()
# passwd_words=[]
# for word in file0:
#     words=word.split()
#     for i in range(len(words)):
#         if 3<=len(words[i])<=7:
#             passwd_words.append(words[i])
# rand_index_1,rand_index_2=randint(0,len(passwd_words)),randint(0,len(passwd_words))
# while not(8<=len(passwd_words[rand_index_1])+len(passwd_words[rand_index_2])<=10):
#     rand_index_1, rand_index_2 = randint(0, len(passwd_words) - 1), randint(0, len(passwd_words) - 1)
# else:
#     print(passwd_words[rand_index_1] + passwd_words[rand_index_2])
#8
# n,m=int(input()),int(input())
# switch=0
# for i in range(n):
#     if i%2==0:
#         print("#"*m)
#     else:
#         if switch%2==0:
#             switch+=1
#             print("."*(m-1)+"#")
#         else:
#             switch += 1
#             print( "#"+"."*(m-1))

