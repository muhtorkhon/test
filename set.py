# key = ['ten','twenty','thirty']
# values = [10,20,30]
# a = dict(zip(key,values))
# print(a)

# a={key[i]:values[i] for i in range(len(key))}
# print(a)

# a = {'a':100,'b':200,'c':300}
# if 200 == a['a'] or 200 == a['b'] or 200 == a['c']:
#     print("bor")
# else:
#     print("yo'q")

# a = {1:10,2:20,3:30,4:55,5:25}
# a.pop(max(a, key=a.get))
# a.pop(min(a, key=a.get))
# print(a)


# d1= {1:10,2:20}
# d2= {3:30,4:40}
# d3= {9:90,7:70}
# b = [d2,d3]
# for i in b:
#     d1.update(i)
# print(d1)


# a = {}
# for i in range(int(input(">>> "))):
#     key = input("keyni kiriting: ")
#     a[key] = int(input('value kiriting: '))
# c=0
# for i in a.values():
#     c += i
# print(c)


# a={}
# for i in range(int(input(">>> "))):
#    key = input("keyni kiriting: ")
#    a[key] = int(input('value kiriting: '))

# b = dict(sorted(a.items(), key=lambda x:x[1],reverse=True))               
# print(b)

#print(dict(sorted(a.items(), key=lambda x: x)))

# my_dict = {'a': 3, 'b': 1, 'c': 2}

# # Saralangan juftliklar ro'yxatidan lug'at yaratish
# sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1]))
# print(sorted_dict)



# a = {
#     "oranges": {"price": 1000, "quantity": 10},
#     "bananas": {"price": 1500, "quantity": 5},
#     "apples": {"price": 1200, "quantity": 800}
# }
# b = 0
# for key,val in a.items():
#     if val['price']*val['quantity'] > b:
#         b = val['price']*val['quantity']
# for key,val in a.items():
#     if val["price"]*val["quantity"] == b:
#         print(key)


# ali = {"music","sports","reading"}
# sara = {"reading","traveling","cooking"}
# diyor = {"sports","music","gaming"}
# # print(ali.union(sara.union(diyor)))
# print(ali.difference(sara.difference(diyor)))


#________________________________________________________________


# 1. Telefon Kitobi
# Masala: Telefon raqamlarini saqlaydigan telefon kitobini tuzing. Lug‘atda ismlarni kalit sifatida, raqamlarni esa qiymat sifatida saqlang. Bunda foydalanuvchi lug‘atga yangi foydalanuvchini qo‘shishi, mavjud foydalanuvchining raqamini yangilashi va foydalanuvchini o‘chirishi mumkin bo‘lsin.

# Topshiriq:

# add_contact(name, number) funksiyasini yozing, bu funksiya yangi foydalanuvchini lug‘atga qo‘shadi.
# update_contact(name, number) funksiyasini yozing, bu funksiya mavjud foydalanuvchining raqamini yangilaydi.
# delete_contact(name) funksiyasini yozing, bu funksiya foydalanuvchini lug‘atdan o‘chiradi.
# find_contact(name) funksiyasini yozing, bu funksiya foydalanuvchining raqamini qaytaradi yoki foydalanuvchi topilmasa, tegishli xabarni ko‘rsatadi.
# 2. Talabalar Baholash
# Masala: Talabalar ro‘yxatini ularning baholari bilan saqlang. Lug‘atda talabaning ismi kalit sifatida, uning baholari ro‘yxati qiymat sifatida saqlansin. Foydalanuvchi talabaning baholarini qo‘shishi, o‘rtacha bahosini hisoblashni amalga oshirishi va eng yuqori yoki eng past bahosini topishi mumkin.

# Topshiriq:

# add_grade(name, grade) funksiyasini yozing, bu funksiya talabaga yangi baho qo‘shadi.
# average_grade(name) funksiyasini yozing, bu funksiya talabaning o‘rtacha bahosini qaytaradi.
# highest_grade(name) funksiyasini yozing, bu funksiya talabaning eng yuqori bahosini qaytaradi.
# lowest_grade(name) funksiyasini yozing, bu funksiya talabaning eng past bahosini qaytaradi.
# 3. Mahsulot Narxlari
# Masala: Do‘kondagi mahsulotlar narxlarini saqlang. Lug‘atda mahsulot nomi kalit sifatida, uning narxi qiymat sifatida saqlansin. Foydalanuvchi mahsulot narxini qo‘shishi, o‘zgartirishi, o‘chirishi va barcha mahsulotlarning o‘rtacha narxini hisoblashni amalga oshirishi mumkin.

# Topshiriq:

# add_product(product_name, price) funksiyasini yozing, bu funksiya mahsulotni lug‘atga qo‘shadi.
# update_price(product_name, price) funksiyasini yozing, bu funksiya mavjud mahsulotning narxini yangilaydi.
# delete_product(product_name) funksiyasini yozing, bu funksiya mahsulotni lug‘atdan o‘chiradi.
# average_price() funksiyasini yozing, bu funksiya barcha mahsulotlarning o‘rtacha narxini qaytaradi.
# 4. Sinflar va Talabalar
# Masala: Bir nechta sinflarni talabalar ro‘yxati bilan saqlang. Lug‘atda sinf nomi kalit sifatida, uning talabalar ro‘yxati qiymat sifatida saqlansin. Foydalanuvchi sinfga talaba qo‘shishi, talabani sinfdan o‘chirishi va sinfdagi barcha talabalarni ko‘rsatishi mumkin bo‘lsin.

# Topshiriq:

# add_student_to_class(class_name, student_name) funksiyasini yozing, bu funksiya sinfga yangi talaba qo‘shadi.
# remove_student_from_class(class_name, student_name) funksiyasini yozing, bu funksiya talabani sinfdan o‘chiradi.
# list_students_in_class(class_name) funksiyasini yozing, bu funksiya sinfdagi barcha talabalarni qaytaradi.
# 5. So‘z Hisobi
# Masala: Berilgan matnda har bir so‘zning nechta marta uchraganini hisoblang. Foydalanuvchi matnni kiritganda, lug‘atni so‘zlarning paydo bo‘lish soni bilan to‘ldiring.

# Topshiriq:

# count_words(text) funksiyasini yozing, bu funksiya matndagi har bir so‘zning uchrash sonini qaytaruvchi lug‘atni qaytaradi.



#1-problem  TELEFON KITOBCHASI
# tel={}
# while int(input("Yangi contact qo'shishni istaysizmi [1]Ha [0]Yo'q: ")):
#     for i in range(int(input('Nechta kontakt saqlamoqchisiz:'))):
#         key = input('Ismni kiriting:')
#         tel[key] = int(input('Raqamni kiriting: '))
#     while int(input("Raqamni yangilamoqchimisiz [1]Ha [0]Yo'q: ")):
#         key = input("Kimning raqamini o'zgartirmoqchisiz:")
#         if key in tel:
#             tel[key] = int(input("Yangi raqam kiriting: "))
#         else:
#             print(f"{key} bu contact mavjud emas")
#             continue
#         break
#     while int(input("Contactdan o'chirmoqchimisiz [1]Ha [0]Yo'q: ")):
#         key = input("Kimni contactdan o'chirmoqchisiz: ")
#         if key in tel:
#             tel.pop(key)
#         else:
#             print(f"{key} bu contact mavjud emas")
#             continue
#         break
#     print("Sizning barcha contactlaringiz")
#     for name,number in sorted(tel.items()):
#         print(f"Ism {name} Raqam {number}")



# tel = {}

# while True:
#     action = int(input("Harakatni tanlang [1] Qo'shish [2] Yangilash [3] O'chirish [4] Barcha kontaktlar [0] Chiqish: "))
    
#     if action == 0:
#         print("Dasturdan chiqilmoqda...")
#         break

#     elif action == 1:
#         name = input('Ismni kiriting: ')
#         number = int(input('Raqamni kiriting: '))
#         tel[name] = number
#         print(f"{name} muvaffaqiyatli qo'shildi.")

#     elif action == 2:
#         name = input("Kimning raqamini o'zgartirmoqchisiz: ")
#         if name in tel:
#             tel[name] = int(input("Yangi raqam kiriting: "))
#             print(f"{name} raqami muvaffaqiyatli yangilandi.")
#         else:
#             print(f"{name} ismi mavjud emas.")

#     elif action == 3:
#         name = input("Kimni contactdan o'chirmoqchisiz: ")
#         if name in tel:
#             tel.pop(name)
#             print(f"{name} kontakt o'chirildi.")
#         else:
#             print(f"{name} ismi mavjud emas.")

#     elif action == 4:
#         if tel:
#             print("Sizning barcha contactlaringiz:")
#             contacts = "\n".join([f"Ism: {name}, Raqam: {number}" for name, number in sorted(tel.items())])
#             print(contacts)
#         else:
#             print("Kontaktlar ro'yxati bo'sh.")

#     else:
#         print("Noto'g'ri amal tanlandi, iltimos qayta urinib ko'ring.")




        