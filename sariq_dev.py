# import os
# import time
# mah = {}
# cop = ''
# print("1.Admin\n2.User\n0.Exit")
# n = int(input(">>> "))
# if n == 1:
#     log = input("Login kiriting: ")
#     while 1:
#         class Uzum:
#             def __init__(self):
#                 self
#             def qosh(self):
#                 Uzum.mah = {}
#                 for i in range(int(input("Nechta yangi maxsulot keldi: "))):
#                     key = input(f"{i+1}-Maxsulotni kiriting: ")
#                     mah[key] = int(input(f"Narxini kiriting: "))
#                 os.system("cls")
#                 for key,vel in mah.items():
#                     print(f"{key} : {vel} so'm")
#                 print("")
#             def ochir(self):
#                 print("Qaysi maxsulotni o'chirmoqchisiz")
#                 a = input("Nomini kiriting: ")
#                 if a in mah:
#                     mah.pop(a)
#                     print(f"{a} <- Bu maxsulot o'chirildi\n")
#                     time.sleep(2)
#                     os.system("cls")
#                     for key,vel in mah.items():
#                         print(f"{key} : {vel} so'm")
#                     print("")
#                 else:
#                     print("Bunday maxsulot mavjud emas")
#                     self.ochir()
#             def updat(self):
#                 print("Qaysi maxsulot narxini o'zgartirasiz")
#                 tov = input("Nomini kiriting: ")
#                 if tov in mah:
#                     mah[tov] = int(input("Yangi narxni kiriting: "))
#                     time.sleep(1)
#                     os.system("cls")
#                     for key,vel in mah.items():
#                         print(f"{key} : {vel} so'm")
#                     print("")
#                 else:
#                     print("Bunday maxsulot mavjud emas")
#                     self.updat()        
#             def korish(self):
#                 for key,vel in mah.items():
#                     print(f"{key} : {vel} so'm")
#                 print("")
#             with open("maxsulot.txt","w") as f:
#                 for nom,narx in mah.items():
#                     f.write(f"{nom} : {narx} so'm\n")
#         a1 = Uzum()
#         print("[1]-Add product\n[2]-Del product\n[3]-Update product\n[4]-My products\n[0]-Exit")        
#         num = int(input(">>> "))
#         if num == 1:
#             a1.qosh()
#         elif num == 2:
#             a1.ochir()
#         elif num == 3:
#             a1.updat()
#         elif num == 4:
#             a1.korish()
#         elif num == 0:
#             print("Amaliyot yakunlandi")
#             break
#         else:
#             print("Eror number\nTry agaen")
#             continue
# elif n == 2:
#     user_login = input("O'z loginingizni yarating: ")
#     while 1:
#         if user_login not in input("Ilovaga kirish uchun loginni qayta kiriting: "):
#             print("Xato login qayta kiriting")
#             continue
#         print("Uzum marketga xush kelibsiz")
#         break
       

        
        



# elif n == 0:
#     print("Dastur yakunlandi")
#     exit()



import json

class Book:
    def __init__(self, id, name, author, count, price):
        self.id = id
        self.name = name
        self.author = author
        self.count = count
        self.price = price

    def write_txt(self, books_list):
        with open("library.txt", "w") as f:
            json.dump([book.__dict__ for book in books_list], f)

    def read_txt(self):
        try:
            with open("library.txt", "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_books(self, books):
        self.write_txt([Book(**b) for b in books])

    def modify_count(self, Id):
        books = self.read_txt()
        for book in books:
            if book["id"] == Id:
                if book["count"] > 0:
                    book["count"] -= 1
                    self.update_books(books)
                    print(f"{book['name']} kitob soni yangilandi: {book['count']}")
                else:
                    print("Kitob tugadi.")
                return
        print("Bunday ID mavjud emas")

    def delete_book(self, Id):
        books = self.read_txt()
        new_books = [book for book in books if book["id"] != Id]
        if len(books) != len(new_books):
            self.update_books(new_books)
            print(f"Kitob ID {Id} o'chirildi.")
        else:
            print("Bunday ID mavjud emas")

# Boshlang'ich kitoblar
books_list = [
    Book(1, "O'tkan kunlar", "Abdulla Qodiriy", 10, 50000),
    Book(2, "Xamsa", "Alisher Navoyi", 8, 70000),
    Book(3, "Kecha va kunduz", "Cho'lpon", 15, 65000),
    Book(4, "Yulduzli tunlar", "Pirimqul Qodirov", 20, 80000),
    Book(5, "Lolazor", "O'tkir Hoshimov", 22, 45000)
]
books_list[0].write_txt(books_list)

# Foydalanuvchi interfeysi
while True:
    print("\n1. Kitob qo'shish")
    print("2. Kitoblarni ko'rish")
    print("3. Kitob sonini kamaytirish (ID bo'yicha)")
    print("4. Kitobni o'chirish (ID bo'yicha)")
    print("0. Dasturdan chiqish")

    choice = input("Tanlovingizni kiriting: ")

    if choice == "1":
        new_id = int(input("Kitob ID sini kiriting: "))
        existing_ids = [book['id'] for book in books_list[0].read_txt()]
        if new_id in existing_ids:
            print("Bunday ID allaqachon mavjud! Iltimos, boshqa ID kiriting.")
            continue
        name = input("Kitob nomini kiriting: ")
        author = input("Kitob muallifini kiriting: ")
        count = int(input("Kitob sonini kiriting: "))
        price = int(input("Kitob narxini kiriting: "))
        new_book = Book(new_id, name, author, count, price)
        books_list.append(new_book)
        books_list[0].write_txt(books_list)
        print("Kitob qo'shildi!")

    elif choice == "2":
        books = books_list[0].read_txt()
        if books:
            for book in books:
                print(f"ID: {book['id']}, Nomi: {book['name']}, Muallif: {book['author']}, Soni: {book['count']}, Narxi: {book['price']}")
        else:
            print("Kitoblar ro'yxati bo'sh!")

    elif choice == "3":
        Id = int(input("Kitob ID sini kiriting: "))
        books_list[0].modify_count(Id)

    elif choice == "4":
        Id = int(input("Kitob ID sini kiriting: "))
        books_list[0].delete_book(Id)

    elif choice == "0":
        print("Dastur tugatildi.")
        break

    else:
        print("Noto'g'ri tanlov! Iltimos, qayta kiriting.")
        