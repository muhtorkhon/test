# f = open("email.txt","r")
# a = set()
# for i in f.read().split("\n"):
#     a.add("."+ i.split(".")[-1])
# f.close  
# print(a)

#2-problem

#f = open("raqam.txt","r")
# a = []
# for i in f.read().split("\n"):
#     a.append(i[:7])
# print(a)

#3-problem telefor raqam takrorlanmagani

# f = open("raqam.txt","r")
# for i in f.read().split("\n"):
#     a=set("".join(i.split(" ",2)[-1].split(" ")))
#     if len(a) == 7:
#         print(''.join(a))

#4-problem FULL_NAME
# a=[]
# f = open("full_name.txt","r")
# for i in f.read().split("\n"):
#     a.append(i.split(" ")[-1])
# a.sort()
# a = "\n".join(a)
# print(a)

#5-problem KARTA RAQAM DAVLAT SONI

# f = open("karta.txt","r")
# a = {}
# ls = []
# for i in f.read().split("\n"):
#     ls.append(i.split(",")[-1])
# for i in ls:
#     a[i] = ls.count(i)
# print(a)

#6-problem VISA BOR DAVLAT SORT

# f = open("karta.txt","r")
# a = []
# for i in f.read().split("\n"):
#     if "visa" in i.split(',')[1]:
#         a.append(i.split(",")[5])
# a.sort()
# a="\n".join(a)
# print(a)

#7-problem KARTA RAQAMDA BARCHA RQAM BORLIGI

# f = open("karta.txt","r")
# g="0123456789"
# for i in f.read().split("\n"):
#     a = []
#     b = []
#     a.append(i.split(",")[0])
#     s = "".join(a)
#     c = "".join(set(s))
#     if len(g) == len(c):
#         print(i)   
        
#8-problem  MAK ADRES

# f = open("internet.txt","r")

# for i in f.read().split("\n"):
#     s="".join(i.split(",")[2:3]).split("-")
#     a=[]
#     for j in s:
#         if j.isalpha():
#             j
#         elif j.isdigit():
#             j
#         else:
#             a.append(j)
#     if len(a)==6:
#         print(i)
# 
# 9-problem  
         
# f = open("xato.txt","r")
# a=[]
# c={}
# for i in f.read().split("\n"):
#     s=''.join(i.split(",")[0:1])
#     a.append(s)
# print(*set(a))   

#10-problem MASHINA BREND

# f = open("mashina.txt","r")
# a=[]
# b={}
# for i in f.read().split("\n"):
#     a.append(i.split(",")[-4])
# for i in a:
#     if i in b:
#         b[i] += 1
#     else:
#         b[i] = 1
# sb = None
# max_count=0
# for i,c in b.items():
#     if c > max_count:
#         max_count = c
#         sb = i
# print(f"Eng ko'p yozilbgan mashina brandi {sb} ({max_count})martta")

# a=[1,3,4,2,7,5,9,43,7]
# f = open("salom.txt","w")
# f.write(f"{' '.join([str(i) for i in sorted(a)])}")
# for i in sorted(a):
#     f.write(f"{str(i)} ")

# with open("salom.txt","w+") as f:
#     f.write(input(">>> "))
#     f.seek(0)
#     for i in f.read().split():
#         if i == i[::-1]:
#             print(i)

# d = open()
# f = open("")
# f1= open("katta.txt","w")

# for i in f.read().split():
#     if i[0].isupper:
#         f1.write(f"{i} ")
# f.close()
#f1.close()