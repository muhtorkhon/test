# class najot:
#     def show(self):
#         print("salom")

# n = najot()
# n.show()


#2-masala


# class animal:
#     def __init__(self,brend,rang):
#         self.marka = brend
#         self.collor = rang
#     def pr(self):
#         print(f"{self.marka} {self.collor}")
# f = animal("Mers","qizil")
# f.pr()


#4-masala

# class car:
#     def __init__(self, brend, name, year):
#         self.brend=brend
#         self.nomi=name
#         self.yil=year
#     def start(self):
#         print(f"{self.brend}\n{self.nomi}\n{self.yil}")
#     def stop(self):
#         print(f"{self.brend}\n{self.nomi}\n{self.yil}")
#     def turn_righte(self):
#         print(f"{self.brend}\n{self.nomi}\n{self.yil}")
#     def turn_back(self):
#         print(f"{self.brend}\n{self.nomi}\n{self.yil}")

# a = car("BMW","x7 i70",2024)
# a.start()

#5-masala

# class talaba:
#     def __init__(self, ism, familya, baho):
#         self.name=ism
#         self.family=familya
#         self.gread=baho

# a = talaba("Ali","Valiyev",75)
# b = talaba("karim","Halimov",60)
# c = talaba("Salim","Qurbonov",55) 

# if a.gread < b.gread and a.gread < c.gread:
#     print(a.name)
# elif b.gread < c.gread:
#     print(b.name)
# else:
#     print(c.name)


# class human:
#     def __init__(self, first_name, last_name, age):
#         self.first=first_name
#         self.last=last_name
#         self.tosh=age
#     def full_name(self):
#         return self.first + self.last

# a = human("Qurbon","Sarbon",34)
# print(a.full_name()) 



# class Talaba:
#     def __init__(self, ism, familya, yosh):
#         self.ism = ism
#         self.familya  = familya
#         self.yosh = yosh
#         self.kurs = 1
#     def info(self):
#         return print(f"{self.ism}\n{self.familya}\n{self.yosh}\n{self.kurs}")
#     def set_kurs(self, bosqich):
#         self.kurs = bosqich
#     def update(self):
#         self.kurs += 1

# class Fan:
#     def __init__(self,nomi):
#         self.nomi = nomi
#         self.talabalar_soni = 0
#         self.talabalar = []

#     def add_student(self,talaba):
#         self.talabalar.append(talaba) 
#         self.talabalar_soni += 1
#     def get_students(self):
#         return [i.info() for i in self.talabalar]

# t1 = Talaba("vali","Aliyev",22)
# t2 = Talaba("Halim","Salimov",34)
# t3 = Talaba("Karim","Qurbonov",19)

# new_fan = Fan("Informatika")
# new_fan.add_student(t2)
# new_fan.add_student(t1)
# new_fan.add_student(t3)
# a = new_fan.get_students()


# class Avto:
#     def __init__(self,brand,modul,rang,narx):
#         self.brand = brand
#         self.modul = modul
#         self.rang = rang
#         self.narx = narx
#         self.km = 0
#     def info(self):
#         print(f"""{self.brand}
# {self.modul}
# {self.rang}
# {self.narx}
# {self.km}""")
#     def set_brand(self,new_brand):
#         self.brand = new_brand
#     def set_modul(self,new_modul):
#         self.modul = new_modul
#     def set_rang(self,new_rang):
#         self.rang = new_rang
#     def set_narx(self,new_narx):
#         self.narx = new_narx
#     def set_km(self,new_km):
#         self.km = new_km

# class Salon:
#     def __init__(self,nomi,manzili):
#         self.nomi = nomi
#         self.manzili = manzili
#         self.avtomobillar = []
#         self.soni = 0
#     def add(self,car):
#         self.avtomobillar.append(car)
#         self.soni += 1
#     def inf(self):
#         return [i.info() for i in self.avtomobillar]
    
# a1 = Avto("BMW","X7","qora",450000)
# a2 = Avto("mers","M800","oq",55000)
# a3 = Avto("chevrolet","Malibu","qora",20000)
# a4 = Avto("tesla","A8","qizil",750000)

# a1.set_km(100)

# av = Salon("Inomarka","Toshkent")
# av.add(a1)
# av.add(a3)
# av.inf()

# class bino:
#     def __init__(self, balandlik,rang):
#         self.balandlik = balandlik
#         self.rang = rang
#     def tekshir(self):
#         if self.balandlik > 50:
#             self.info()
#     def info(self):
#         print(f"Balandlik {self.balandlik}\nRang {self.rang}")

# a1 = bino(45,"qizil")
# a2 = bino(50,"oq")
# a3 = bino(55,"ko'k")
# a4 = bino(65,"qora")
# lts = [a1,a2,a3,a4]
# for i in lts:
#     i.tekshir()

# class human:
#     def __init__(self,name,age,profession,heighte,weight,single):
#         self.name = name
#         self.age = age
#         self.profession = profession
#         self.heighte = heighte
#         self.weight = weight
#         self.single = single
#     def get_name(self):
#         return self.name
#     def get_age(self):
#         return self.age
#     def get_profession(self):
#         return self.profession
#     def get_heighte(self):
#         return self.heighte
#     def get_weight(self):
#         return self.weight
#     def get_single(self):
#         return self.single
    
# s1 = human("frefnk",28,"developer",1.75,70,"married")
# print(s1.get_name())

# import math

# class Circle:
#     def __init__(self,radius,color):
#         self.radius = radius
#         self.color = color
#     def get_radius(self):
#         return self.radius
#     def set_radius(self,rad):
#         self.radius = rad
#     def get_color(self):
#         return self.color
#     def set_color(self,color):
#         self.color = color
#     def get_area(self):
#         return math.pi * self.radius * self.radius
#     def get_circumference(self):
#         return 2 * math.pi * self.radius
#     def info(self):
#         print(f"{self.radius}\n{self.color}\n{self.get_area()}\n{self.get_circumference()}")

# a1 = Circle(50,"oq")
# a1.get_area()
# a1.get_circumference()
# a1.info()

