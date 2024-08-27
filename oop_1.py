#from datetime import data
# class Drug:
#     def __init__(self,nomi,sanasi):
#         self.nomi = nomi
#         self.sanasi = sanasi
#     def get_time(self,bugun):
#         return bugun - self.sanasi
# a1 = Drug("kupen",2020)
# print(a1.get_time(2024))


# class Bookstar:
#     def __init__(self,ism,yosh,k_nom,k_narx):
#         self.ism = ism
#         self.yosh = yosh
#         self.k_nom = k_nom
#         self.k_narx = k_narx
#     def get_price(self):
#         return self.k_narx * (self.yosh/100)

# a1 = Bookstar("jasur",20,"Iymon",50000)
# print(a1.get_price())


# class Transport:
#     def __init__(self,fuel,model,max_speed):
#         self.fuel = fuel
#         self.model = model
#         self.max_speed = max_speed
#     def get_info(self):
#         print(f"MODEL:{self.model}\nMAX SPEED:{self.max_speed}\nFUEL:{self.fuel}")

# a1 = Transport("A 95",)


# class odam:
#     def __init__(self,ism,familya,yosh,kasb):
#         self.ism = ism
#         self.familya = familya
#         self.yosh = yosh
#         self.kasb = kasb

#     def info(self):
#         return f"""ism:{self.ism}
# familya:{self.familya}
# yosh:{self.yosh}
# kasb:{self.kasb}"""
# class talaba(odam):
#     def __init__(self,ism,familya,yosh,kasb,kurs,stipendiya):
#         super().__init__(ism,familya,yosh,kasb)
#         self.kurs = kurs
#         self.stipendiya = stipendiya
#     def info(self):
#         return f"""{super().info()}
# kurs:{self.kurs}
# stipendiya:{self.stipendiya}"""

# a1 = talaba("Baxrom","qurbonov",32,"usta",2,10000)
# print(a1.info())


# class Transport:
#     def __init__(self,benzin):
#         self.benzin = benzin

# class car(Transport):
#     def __init__(self,benzin,tezlik):
#         super().__init__(benzin)
#         self.tezlik = tezlik
#     def km(self):
#         return self.benzin * self.tezlik
# a1 = car(10,100)
# print(a1.km())


# class Papulation:
#     def __init__(self,ism,yosh,jins):
#         self.ism = ism
#         self.yosh = yosh
#         self.jins = jins
#     def get_info(self):
#         if self.jins in 'erkak' and self.yosh > 50:
#             print(f"Janob {self.ism}")
#         elif self.jins in 'ayol' and self.yosh > 50:
#             print(f"{self.ism} xonim")

# a1 = Papulation("Jek",51,"erkak")
# a2 = Papulation("Anna",58,"ayol")
# a3 = Papulation("Uvlisn",34,"erkak")
# a4 = Papulation("Mariya",50,"ayol")
# a5 = Papulation("Smit",52,"erkak")
# a = [a1,a2,a3,a4,a5]
# for i in a:
#     i.get_info()


# class My(list):
#     def remove(self,a):
#         while a in self:
#             super().remove(a)
            
# lst = My((1,2,3,3,3,4,5,6,5,5,6,7,1,8))
# print(lst)
# lst.remove(int(input(">>> ")))
# print(lst)


# class Mylist(list):
#     def append(self, a):
#         if a in self:
#             print("Element Dublication Error")
#             exit()
#         elif a not in self:
#             super().append(a)


# lts = Mylist((1,2,3,4,5))
# print(lts)
# lts.append(int(input(">>> ")))
# print(lts)


# class book:
#     def __init__(self,nom,mul,yil):
#         self.nom = nom
#         self.mul = mul
#         self.yil = yil
# class bs(book):
#     def __init__(self,nom,mul,yil,narx):
#         super().__init__(nom,mul,yil)
#         self.narx = narx
#     def info(self):
#         return f"""{self.nom}
# {self.mul}
# {self.yil}
# {self.narx}"""
#     def get_g(self,yil):
#         if yil - self.yil > 5:
#             self.narx = self.narx-(self.narx//10)*2
#             return self.info()
        
# a1 = bs("iymon","Shayx",2000,40000)
# print(a1.get_g(2024))

class ProductSelectionApp:
    def __init__(self):
        self.products = self.load_products_from_file("products.txt")

    def load_products_from_file(self, filename):
        products = []
        try:
            with open(filename, "r", encoding="utf-8") as f:
                for line in f:
                    parts = line.strip().split(",")
                    if len(parts) == 3:
                        product_id, name, price = parts
                        try:
                            price = int(price)
                            products.append({"id": int(product_id), "name": name, "price": price})
                        except ValueError:
                            print(f"Xato: '{line.strip()}' narxi raqam emas.")
                    else:
                        print(f"Xato: '{line.strip()}' noto'g'ri formatda.")
        except FileNotFoundError:
            print(f"Xato: '{filename}' fayl topilmadi.")
        except Exception as e:
            print(f"Xato: {e}")
        return products

    def display_products(self):
        print("Mahsulotlarni tanlang:")
        for product in self.products:
            print(f"{product['id']}. {product['name']} - {product['price']} so'm")

    def select_product(self):
        with open("korzinka.txt", "a", encoding="utf-8") as add_korina:
            while True:
                try:
                    choice = int(input("Tanlash uchun mahsulot raqamini kiriting (chiqish uchun 0 kiriting): "))
                    if choice == 0:
                        print("Dasturdan chiqildi.")
                        break
                    else:
                        selected_product = next((p for p in self.products if p['id'] == choice), None)
                        if selected_product:
                            print(f"Siz {selected_product['name']} ni tanladingiz. Narxi: {selected_product['price']} so'm")
                            add_korina.write(f"{selected_product['name']},{selected_product['price']}\n")
                        else:
                            print("Noto'g'ri tanlov! Iltimos, qayta urinib ko'ring.")
                except ValueError:
                    print("Iltimos, raqam kiriting!")

    def sum_korzinka(self):
        total_sum = 0
        try:
            with open("korzinka.txt", "r", encoding="utf-8") as kf:
                for line in kf:
                    parts = line.strip().split(",")
                    if len(parts) == 2:
                        try:
                            price = int(parts[1])
                            total_sum += price
                        except ValueError:
                            print(f"Xato: '{line.strip()}' narxi raqam emas.")
        except FileNotFoundError:
            print("Xato: 'korzinka.txt' fayl topilmadi.")
        except Exception as e:
            print(f"Xato: {e}")
        print(f"Savatdagi jami narx: {total_sum} so'm")

# Dasturdan foydalanish:
app = ProductSelectionApp()
if app.products:
    app.display_products()
    app.select_product()
    app.sum_korzinka()




class User:
    def __init__(self, username, password, email):
        self.username = username
        self.__password = password  
        self.email = email

    def login(self, username, password):
        if self.username == username and self.__password == password:
            print(f"Welcome {self.username}!")
        else:
            print("Login xato.")

    def update_email(self, new_email):
        self.email = new_email
        print(f"Email yangilandi: {self.email}")

    def update_password(self, old_password, new_password):
        if self.__password == old_password:
            self.__password = new_password
            print("Parol yangilandi")
        else:
            print("Eski parol noto'g'ri")

    def get_info(self):
        return f"Username: {self.username}, Email: {self.email}"

print("[1] Hisob yaratish ")
print("[2] Hisobni yangilash")

while True:
    inp = int(input("Tanlang: "))
    if inp == 1:
        user1 = User(input("Ismingizni kiriting: "), input("Parolni kiriting: "), input("Emailni kiriting: "))
        print("Hisob yaratildi!")
    elif inp == 2:
        if user1 is not None:
            if user1.login(input("Ismingizni kiriting: "), input("Parolni kiriting: ")):
                user1.update_email(input("Yangi emailni kiriting: "))
                user1.update_password(input("Eski parolni kiriting: "), input("Yangi parolni kiriting: "))
        else:
            print("Avval hisob yarating.")
    else:    
        break

if user1 is not None:
    print(user1.get_info())
else:
    print("Hisob yaratilmadi.")
    

