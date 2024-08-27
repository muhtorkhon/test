# a = [1,4,7,9,2]
# max = 0
# min = a[0]
# for i in a:
#     if isinstance(i,int):
#         if i > max:
#             max = i
#         elif i < min:
#             min = i
# print(f"max {max}\nmin {min}")


#9 masala


# n = ['salom','kim','niman','qani','aba']
# c = 0
# for i in n:
#     if i[0] == i[-1]:
#         c += 1
# print(c)


#10 masala

# n = [12,3,5,9,4,8,10]
# for i in n:
#     if i % 2 == 1:
#         print(i)

#5 masala
# ls =[]
# j = 0
# ls1=[]
# for i in range(1000):
#     ls1.clear()
    
#     for j in range(1000):
#         k = 1
#         while k>j:
#             if j%k==0:
#                 ls.append(k)
#             k+=1
#     if sum(ls)==i and sum(ls1)==j:
#         print(i)
#         print() 


#1-masala shaxmat doskasi rangi

# a = int(input('Enter number:'))
# b = int(input('Enter number:'))
# if (a + b)% 2 == 0:
#     print("qora")
# else:
#     print("oq")

#2-masala
# n = int(input('Enter number:'))
# a=1
# while a <= n:
#     b=1
#     count=0
#     while b <= a:
#         if a%b == 0:
#             count += 1
#         b += 1
#     if count == 9:
#         print(a, end=' ')
#     a += 1

#3-masala raqamlar 3 bolgan sonlar

# n = int(input('Enter number:'))
# count = 0
# for a in range(1,n):
#     b=a
#     while a != 0:
#         c = a%10
#         if c == 3:
#             print(b, end=' ')
#             count += 1
#         a //= 10
# print(f" soni {count}")

#6-masala ekub va ekuk

# def ekub(a,b):
#     while b:
#         a,b = b,a%b
#     return a
# a = int(input('>>> '))
# b = int(input(">>> "))
# d=a
# s=b
# natija = ekub(a,b)
# r=(d*s)//natija
# print(f"{a}va{b} sonlari EKUBI:{natija}")
# print(f"ekuk {r}")

#9-masala 10 ni 2likka o'tkaz
    
# n = int(input('>>> '))
# a=[]
# while n != 0:
#     a.insert(0, str(n%2))
#     n //= 2
# print("".join(a))

# 10-masala sumni aniqla

# b=[]
# while 1:
#     i = input('>>> ')
#     if i == 'c':
#         break
#     b.append(int(i))
# print(sum(b))
b = []
while 1:
    a = (input('>>> '))
    if a == 'exit':
        break
    b.append(a)
print(b)
