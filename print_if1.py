#print(a:=int(input("asosni kirit:")), b:=int(input("daraja kirit:")),a**b)

#print(a:=int(input("kunni kiriting:")), b:=int(input("oyni kiriting:")),"\n",f"Brithday is,{a}-{b}!!!")

# son = int(input("son kiriting:"))
# c = son % 10
# son //= 10
# r = son % 10
# son //= 10
# t = son % 10
# print(c+r+t)


#print(a:= int(input("birinchi sinni kiriting:")),b:= int(input("ikkinchi sinni kiriting:")),(a+b)/2)

#print(a:=int(input("Son kiriting:")),'\n',f"{(a%10)*10 + (a//10)}")

#1 problem

#print(a:=int(input("son kiriting:")),a//1000)

#2 problem

#print(n:=int(input("Sekuntni kiriting:")),"\n","minut otdi", n // 60)

#3 problem

#print(n:=int(input("Sekuntni kiriting:")),"\n","Soat o'tdi", n // 3600 )

#4 problem

#print(n:=int(input("Sekuntni kiriting:")),"\n",f"minut otdi {n//60}\nSekunt o'tdi {n%60}")

#5 problem

#print(n:=int(input("Sekuntni kiriting:")),"\n",f"Soat o'tdi {n//3600}\nSekunt o'tdi {n%3600}")

# problem

#print(n:=int(input("Sekuntni kiriting:")),"\n",f"{n // 3600} Soatu || {(n%3600)//60} Minutu || {n%60} Sekunt o'tdi")

#print("Ism", name:=input("Enter name:"),"\n","Family",family:=input("Enter family:"))

# a = int(input("Enter the first number:"))
# c = input("Enter operator:")
# b = int(input("Enter the second number:"))
# print(a+b) if c == '+' else print(a-b) if c == '-' else print(a*b) if c == '*' else print(a/b)

# char = input("Enter letter:")
# print (ord(char))

# a = input("Enter text:")
# print(len(a)**3)

# a = int(input("Enter number:"))
# c = 0
# for i in range(1, a):
#     if a%i == 0:
#         c += i
# print("Mukammal son") if c == a else print("Mukammal son emas") 


# n = int(input("Enter number:"))
# s = n
# c = 0
# while n != 0:
#     c = (c*10) + (n%10)
#     n //= 10
# print(c)
# print("Palindrome son") if c == s else print("Palindrome emas")

#print("The largest digit is:", max(int(d) for d in input("Enter a number: ")))

# n = int(input("son kiriting:"))
# c = n
# s = 0
# while c != 0:
#     s += (c % 10)**3
#     c //= 10
# print("Armstrong son") if s == n else print("emas")
a = 0
b = 0   
for i in range(1,11):
    son = [i]. int(input("son kiriting:"))
    a = son = [i]
for i in range(1,11):
    if son > a:
        a = son



