from database import maxsulotlar

savat = []

# Barcha maxsulotlarni ko'rish funksiyasi
def barcha_maxsulotlar():
    for maxsulot in maxsulotlar:
        print(f"ID: {maxsulot['id']}, Nomi: {maxsulot['nomi']}, Narxi: {maxsulot['narxi']}$")

# Maxsulot tanlash va savatga qo'shish funksiyasi
def savatga_qosh(id):
    for maxsulot in maxsulotlar:
        if maxsulot['id'] == id:
            savat.append(maxsulot)
            print(f"Maxsulot savatga qo'shildi: {maxsulot['nomi']}")
            return
    print(f"Maxsulot topilmadi: ID {id}")

# Savatdagi maxsulotlarni ko'rish funksiyasi
def savatni_kor():
    if savat:
        print("Savatdagi maxsulotlar:")
        for maxsulot in savat:
            print(f"{maxsulot['nomi']}, Narxi: {maxsulot['narxi']}$")
    else:
        print("Savat bo'sh!")

# To'lovni amalga oshirish funksiyasi
def tolov():
    jami = sum([maxsulot['narxi'] for maxsulot in savat])
    if jami > 0:
        print(f"To'lov qabul qilindi. Jami: {jami}$")
        savat.clear()
    else:
        print("Savat bo'sh, to'lov amalga oshirib bo'lmaydi.")
