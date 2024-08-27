#1-m

# t = (2,4,6,8)
# print(sum(t))

#2-m

# t = (3,5,1,6,8,9)
# max = max(t)
# min = min(t)
# print(max-min)

#3-m

# t = (3,5,6,1,7,9,4)
# r = list(t)
# a = max(r)
# r.remove(a)
# t = tuple(r)
# print(t)

#4-m

# new=[]
# t = ('salom','kim','nnimani','fargona')
# l = list(t)
# new = [i for i in l if len(i)>5]
# print(new)

#5-m

# new = []
# t = [(1,3),(0,2,0),(1,1,1),(0,4),(1,9)]
# for i in t:
#     new.append(sum(i))
# print(new)

#6-m

# t = [(1,2,3),(2,2),(3,0,0)]
# a = sorted(t, key=lambda x: sum([i for i in x]))
# print(a)

#7-m

# n = [[1,2,3],[4,5,6],[9,27],[2,0,10],[0,1],[1],[2,2,2]]
# max=sum(n[0])
# index=0
# for i in range(1,len(n)):
#     if max < sum(n[i]):
#         max = sum(n[i])
#         index = i
# print(max, n[index])

#8-m 
# a=[]
# n = [(1,2),(2,3),(3,4)]
# a = [list(i) for i in n]
# print(a)

#9-m

# a = ('ada',212,'folse',4671,'aziza')
# b = [str(i)for i in a]
# [print(f"{i} palindrom") if i == i[::-1] else print(f"{i} palindrom emas") for i in b]

#10-m

# a = [9,9,9,9] 
# b = [int(i)for i in list(str(int(''.join([str(i) for i in a]))+1))]
# print(b)

#11-m

# a = [1,1,2,3,5,8,13,21,34,55,89]
# b = [1,2,3,4,5,6,7,8,9,10,11,12,13]
# c = [j for i in a for j in b if i == j]
# print(c)

#12-m

#a = [int(i)for i in list(input('>>> ')]
# count = 0
# count1=0
# count2=0
# osish = a[0]
# kamayish = a[0]
# for i in a:
#     if i > osish:
#         count+=1
#     if i < kamayish:
#         count1+=1
# while 1:   
#     if len(a)-1 == count:
#         print("O'sish")
#         break
#     elif len(a)-1 == count1:
#         print("kamayish")
#         break
#     else:    
#         print("aralash")
#         break

#13-m
# c=[]
# s=[]
# a = [(1,2),(3,4),(8,9)]
# for i,t in a:
#     c.append(i)
#     s.append(t)
# print(c,s)

# n = [[1,2,3],[4,5,6],[9,27],[2,0,10],[0,1],[1],[2,2,2]]
# a = max(n, key=lambda x:sum(x) if len(x) > 1  else -1)
# print(a)

# b=[]
# s=[]
# a = [(0,2,0,0),(0,3,2,2),(1,3,2,4,3),(4,1,2,4)]
# b = [list(i)for i in a]
# for i in b:
#     c=[]
#     for j in i:
#         c.append(i.count(j))
#     s.append(tuple(c))
# print(s)

# 1. O'rta darajali masala: O'quvchilar ballarini qayta ishlash
# Sizga bir nechta o'quvchilarning ismlari, baholari va ularga tegishli fanlarning ro'yxati berilgan. Masalan:

# python
# Copy code
# oquvchilar = [
#     ("Ali", {"math": 85, "physics": 90, "chemistry": 78}),
#     ("Said", {"math": 92, "physics": 88, "chemistry": 85}),
#     ("Laylo", {"math": 70, "physics": 75, "chemistry": 80}),
# ]
# Vazifa:

# Har bir o'quvchi uchun o'rtacha ballni hisoblang va tuple shaklida qaytaring (("Ism", o'rtacha ball)).
# O'rtacha ball bo'yicha ro'yxatni kamayish tartibida saralang.
# Har bir o'quvchi uchun ballari eng yuqori bo'lgan fanni toping va uni o'quvchi ismi bilan birga qaytaring (("Ism", "Fan")).
# 2. Yuqori darajali masala: Ishchilar ma'lumotlarini tahlil qilish
# Sizga kompaniya xodimlari haqida ma'lumotlar berilgan. Har bir xodim uchun ism, lavozim, yoshi va maoshlari ro'yxati tuple ko'rinishida taqdim etilgan. Misol:

# python
# Copy code
# xodimlar = [
#     ("Olim", "Muhandis", 28, 3500),
#     ("Kamola", "Dizayner", 24, 2800),
#     ("Jasur", "Boshqaruvchi", 45, 5000),
#     ("Madinabonu", "Muhandis", 30, 3600),
#     ("Farhod", "Dizayner", 29, 2900),
# ]
# Vazifa:

# Har bir lavozim uchun o'rtacha maoshni hisoblang va natijani lug'at shaklida qaytaring ({"Lavozim": o'rtacha maosh}).
# Maoshi eng yuqori bo'lgan xodimni toping va uning ismi va lavozimini qaytaring.
# Har bir lavozimda yoshi 30 dan yuqori bo'lgan xodimlar ro'yxatini tuzing.

o=[
("Ali", {"math": 85, "physics": 90, "chemistry": 78}),
("Said", {"math": 92, "physics": 88, "chemistry": 85}),
("Laylo", {"math": 70, "physics": 75, "chemistry": 80}),]

a = [list(j)for i in o for j in i]
print(a)
