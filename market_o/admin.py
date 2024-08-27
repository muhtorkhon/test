from database import maxsulotlar

# Maxsulot qo'shish funksiyasi
def maxsulot_qosh(nomi, narxi):
    yangi_id = len(maxsulotlar) + 1
    maxsulotlar.append({"id": yangi_id, "nomi": nomi, "narxi": narxi})
    print(f"Maxsulot qo'shildi: {nomi}, Narxi: {narxi}$")

# Maxsulot o'chirish funksiyasi
def maxsulot_ochir(id):
    for maxsulot in maxsulotlar:
        if maxsulot['id'] == id:
            maxsulotlar.remove(maxsulot)
            print(f"Maxsulot o'chirildi: {maxsulot['nomi']}")
            return
    print(f"Maxsulot topilmadi: ID {id}")

# Maxsulot narxini o'zgartirish funksiyasi
def narxni_ozgartir(id, yangi_narx):
    for maxsulot in maxsulotlar:
        if maxsulot['id'] == id:
            maxsulot['narxi'] = yangi_narx
            print(f"Maxsulot narxi o'zgartirildi: {maxsulot['nomi']}, Yangi narx: {yangi_narx}$")
            return
    print(f"Maxsulot topilmadi: ID {id}")

# Barcha maxsulotlarni ko'rish funksiyasi
def barcha_maxsulotlar():
    for maxsulot in maxsulotlar:
        print(f"ID: {maxsulot['id']}, Nomi: {maxsulot['nomi']}, Narxi: {maxsulot['narxi']}$")

# Maxsulotni ID orqali qidirish funksiyasi
def maxsulot_top(id):
    for maxsulot in maxsulotlar:
        if maxsulot['id'] == id:
            print(f"ID: {maxsulot['id']}, Nomi: {maxsulot['nomi']}, Narxi: {maxsulot['narxi']}$")
            return
    print(f"Maxsulot topilmadi: ID {id}")
