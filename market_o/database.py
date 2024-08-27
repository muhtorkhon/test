# Maxsulotlar ro'yxati (id, nomi, narxi)
maxsulotlar = [
    {"id": 1, "nomi": "Telefon", "narxi": 500},
    {"id": 2, "nomi": "Noutbuk", "narxi": 1000},
]

# Admin ro'yxati (faqat bitta admin uchun sodda ro'yxat)
adminlar = [{"username": "admin", "password": "1234"}]

# Adminni tekshirish funksiyasi
def admin_tekshir(username, password):
    for admin in adminlar:
        if admin['username'] == username and admin['password'] == password:
            return True
    return False
