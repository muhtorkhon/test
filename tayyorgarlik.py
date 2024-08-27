# def baholash(isimlar):
#     dic = {}
#     while isimlar:
#         ism = isimlar.pop()
#         n = int(input(f"{ism} nimg bahosini qo'ying: "))
#         dic[ism] = n
#     return dic

# def katta(isimlar):
#     e=[]
#     for i in isimlar:
#         e.append(i.title())
#     return e

# talablar = ['husan','hasan','karim','halim']
# asd = baholash(talablar[:])
# print(asd)
# print(katta(talablar))

#OOP

# class User:
#     def __init__(self,ism,foydalanuvchi,familya,email,yil):
#         self.ism = ism
#         self.foydalanuvchi = foydalanuvchi
#         self.familya = familya
#         self.email = email
#         self.yil = yil
#     def get_info(self):
#         dct={
#             "Foydalanuvchi":self.foydalanuvchi,
#             "Ismi":self.ism,
#             "Familyasi":self.familya,
#             "Email":self.email,
#             "Tug'ilgan yili":self.yil
#         }
#         return dct

    
# a1 = User("Karim","karim1994","Halimov","karimhalimov@gmail.com",1994)
# a1.get_info()



# class Avto:
#     def __init__(self,model,rang,korobka,narx):
#         self.model = model
#         self.rang = rang
#         self.korobka = korobka
#         self.narx = narx
#         self.km = 0
#     def get_info(self):
#         dct={
#             "Model":self.model,
#             "Rang":self.rang,
#             "Korobka":self.korobka,
#             "Narx":self.narx,
#             "Klametr":self.km
#         }
#         return dct
#     def set_metod(self,rang,narx):
#         self.rang = rang
#         self.narx = narx
#     def updat_km(self,km):
#         self.km += km

# class Avtosalon:
#     def __init__(self,salon_nomi,manzil):
#         self.salon_nomi = salon_nomi
#         self.manzil = manzil
#         self.avtomobillar = []
#         self.avtolar_soni = 0
#     def update_avto(self,avto):
#         self.avtomobillar.append(avto)
#         self.avtolar_soni += 1
#     def get_avto_salon(self):
#         return [i.get_info() for i in self.avtomobillar]
#     def add_avto_count(self):
#         return self.avtolar_soni
# a1 = Avto("BMW X7","Qora","Avtomat",350000)
# a2 = Avto("Mersides Bens","Qizil","Mexanika",250000)
# a3 = Avto("Malibu","Oq","Avtomat",35000)
# s1 = Avtosalon("Inomarka","Chilonzor")
# s1.update_avto(a1)
# a1.updat_km(450)
# print(s1.get_avto_salon())
# print(s1.add_avto_count())


# class Shaxs:
#     def __init__(self,ism,familya,pasport,yil,jins):
#         self.ism = ism
#         self.familya = familya
#         self.pasport = pasport
#         self.yil = yil
#         self.jins = jins
#     def get_info(self):
#         info = f"{self.ism.title()} {self.familya.title()}. "
#         info += f"Pr {self.pasport}, {self.yil}, {self.jins}"
#         return info
#     def get_age(self,yil):
#         return yil - self.yil
    
# class Talaba(Shaxs):
#     def __init__(self,ism,familya,pasport,yil,jins,id,kurs):
#         super().__init__(ism,familya,pasport,yil,jins)
#         self.id = id
#         self.kurs = kurs
#         self.fanlar = []
#     def get_info(self):
#         info = f"{self.ism} {self.familya}. "
#         info += f"Pr {self.pasport} {self.yil}, "
#         info += f"{self.jins} {self.id} {self.kurs}, "
#         return info
#     def fanga_yozil(self,obj):
#         self.fanlar.append(obj)
#     def remove_fan(self,fan):
#         if fan in self.fanlar:
#             self.fanlar.remove(fan)
#         else:
#             print("Siz bu fanga yozilmagansiz")
# class Fan:
#     def __init__(self,f_nomi):
#         self.f_nomi = f_nomi

# class Professor(Talaba):
#     def __init__(self,ism,familya,pasport,yil,jins,id,kurs,ilmiy_ish,kashfiyot,dars_berish):
#         super().__init__(ism,familya,pasport,yil,jins,id,kurs)
#         self.ilmiy_ish = ilmiy_ish
#         self.kashfiyot = kashfiyot
#         self.dars_berish = dars_berish
#     def get_info(self):
#         info = f"{super().get_info()}"
#         info += f"{self.ilmiy_ish} {self.kashfiyot} "
#         info += f"{self.dars_berish}"
#         return info


    
# class Manzil:
#     def __init__(self,viloyat,tuman,qishloq,kocha,uy):
#         self.viloyat = viloyat
#         self.tuman = tuman
#         self.qishloq = qishloq
#         self.kocha = kocha
#         self.uy = uy
#     def get_manzil(self):
#         manzil = f"{self.viloyat}, {self.tuman}, "
#         manzil += f"{self.qishloq}, {self.kocha}, {self.uy}"
#         return manzil
    
# talaba = Manzil("Farg'ona","Quva","Qaqir","Xo'ja",111)
# a2 = Professor("karim","halimov","AF1234567",1996,"erkak",890980,3,"Dissertatsiya","Fizik xossalar","Fizik ustoz")
# print(a2.get_info())
























