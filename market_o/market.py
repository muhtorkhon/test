import admin
import user
from database import admin_tekshir

# Admin menyusi
def admin_menu():
    while True:
        print("\nAdmin menyusi:")
        print("1. Maxsulot qo'shish")
        print("2. Maxsulot o'chirish")
        print("3. Maxsulot narxini o'zgartirish")
        print("4. Barcha maxsulotlarni ko'rish")
        print("5. Maxsulotni ID bo'yicha qidirish")
        print("0. Chiqish")

        tanlov = input("Tanlang: ")

        if tanlov == "1":
            nomi = input("Maxsulot nomi: ")
            narxi = int(input("Maxsulot narxi: "))
            admin.maxsulot_qosh(nomi, narxi)
        elif tanlov == "2":
            id = int(input("Maxsulot ID: "))
            admin.maxsulot_ochir(id)
        elif tanlov == "3":
            id = int(input("Maxsulot ID: "))
            yangi_narx = int(input("Yangi narx: "))
            admin.narxni_ozgartir(id, yangi_narx)
        elif tanlov == "4":
            admin.barcha_maxsulotlar()
        elif tanlov == "5":
            id = int(input("Maxsulot ID: "))
            admin.maxsulot_top(id)
        elif tanlov == "0":
            break

# User menyusi
def user_menu():
    while True:
        print("\nUser menyusi:")
        print("1. Barcha maxsulotlarni ko'rish")
        print("2. Maxsulotni savatga qo'shish")
        print("3. Savatni ko'rish")
        print("4. To'lovni amalga oshirish")
        print("0. Chiqish")

        tanlov = input("Tanlang: ")

        if tanlov == "1":
            user.barcha_maxsulotlar()
        elif tanlov == "2":
            id = int(input("Maxsulot ID: "))
            user.savatga_qosh(id)
        elif tanlov == "3":
            user.savatni_kor()
        elif tanlov == "4":
            user.tolov()
        elif tanlov == "0":
            break

# Asosiy dastur
def main():
    print("Online Marketga xush kelibsiz!")
    while True:
        print("\nKirish turi:")
        print("1. Admin")
        print("2. User")
        print("0. Dasturni yakunlash")

        tanlov = input("Tanlang: ")

        if tanlov == "1":
            username = input("Username: ")
            password = input("Password: ")
            if admin_tekshir(username, password):
                admin_menu()
            else:
                print("Login yoki parol xato!")
        elif tanlov == "2":
            user_menu()
        elif tanlov == "0":
            print("Dastur tugadi!")
            break

if __name__ == "__main__":
    main()
