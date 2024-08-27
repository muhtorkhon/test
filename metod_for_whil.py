# n = int(input("Enter number:"))
# i = 1
# while i <= n:
#     f = 1
#     while f <= i:
#         print("*", end=" ")
#         f += 1
#     print()
#     i += 1


# n = int(input("Enter number:"))
# m = int(input("Enter number:"))
# k=1
# for i in range(1,n+1,1):
#     s=0
#     for j in range(1, m+1,1):
#         print(f"{k}+",end=" ")
#         s+=k
#         k+=1
#     print(f"={s}")



# a = input("Sana kiriting:")
# b = input("2-Sanani kiriting:")
# a,b = b[:3]+a[3:5]+b[5:],a[:3]+b[3:5]+a[5:]
# print(f"A -> {a}\nB -> {b}")
        
# a = input("Enter text:")
# b = input("Enter text:")
# a = a[:]+'+Nuriyaxon+'+b[:]
# print(a)

# n = int(input("Enter number:"))
# i = 1
# while i <= n:
#     a = '*'
#     a = a * i
#     print(a)
#     i += 1

# matn = input("Enter text:")
# harf=0
# raqam=0
# for i in matn:
#     if i.isalpha():
#         harf +=1
#     elif i.isdigit():
#         raqam +=1
# print(f"harflar {harf}ta\nraqamlar {raqam}ta")

# def fibonacci(n):
#     a, b = 0, 1
    
#     for _ in range(n):
#         print(a, end=' ')
#         a, b = b, a + b
# n = int(input("n qiymatini kiriting: "))
# fibonacci(n)


# n = int(input('Enter number:'))
# i = 1
# while i <= n:
#     j = 1
#     c = 0
#     while j <= i:
#         if i % j == 0:
#             c += 1
#         j += 1
#     if c == 2:
#         print(i, end=" ")
#     i += 1


# O'rta darajadagi masalalar:
# Stringni teskari o'girish:

# Berilgan stringni teskari qilib chiqaring.
# Misol: "hello" -> "olleh"
# Stringdagi so'zlarni sanash:

# Berilgan stringda nechta so'z borligini aniqlang.
# Misol: "This is a sample sentence." -> 5
# Stringdagi unlilarni sanash:

# Berilgan stringda nechta unli harf borligini aniqlang.
# Misol: "hello world" -> 3
# Stringni katta harflar bilan yozish:

# Berilgan stringni barcha harflarini katta harfga o'giring.
# Misol: "hello world" -> "HELLO WORLD"
# Stringdagi raqamlarni sanash:

# Berilgan stringda nechta raqam borligini aniqlang.
# Misol: "There are 123 apples" -> 3
# Murakkab darajadagi masalalar:
# Palindrome stringni tekshirish:

# Berilgan string palindrome ekanligini tekshiring.
# Misol: "madam" -> True, "hello" -> False
# Stringdagi so'zlarni teskari o'girish:

# Berilgan stringdagi har bir so'zni teskari qilib chiqaring.
# Misol: "hello world" -> "olleh dlrow"
# Stringdan takroriy belgilarni olib tashlash:

# Berilgan stringdan barcha takroriy belgilarni olib tashlang.
# Misol: "hello" -> "helo"
# Stringdagi so'zlarning bosh harfini katta qilish:

# Berilgan stringdagi har bir so'zning bosh harfini katta qiling.
# Misol: "hello world" -> "Hello World"
# Stringni shifrlash (Caesar cipher):

# Berilgan stringni Caesar cipher bilan shifrlang (harflarni k harfga siljitish).
# Misol: "abc" -> "def" (k = 3)
# Stringdagi raqamlarni qo'shish:

# Berilgan stringdagi barcha raqamlarni qo'shib, yig'indisini chiqaring.
# Misol: "a1b2c3" -> 6
# Stringdan maxsus belgilarni olib tashlash:

# Berilgan stringdan barcha maxsus belgilarni olib tashlang.
# Misol: "hello@world!" -> "helloworld"
# Stringdagi eng uzun so'zni topish:

# Berilgan stringdagi eng uzun so'zni aniqlang.
# Misol: "The quick brown fox" -> "quick"
# Stringni base64 formatiga o'girish:

# Berilgan stringni base64 formatiga o'giring.
# Misol: "hello" -> "aGVsbG8="
# Stringdagi katta va kichik harflarni o'zaro almashtirish:

# Berilgan stringdagi katta harflarni kichik, kichik harflarni katta qilib almashtiring.
# Misol: "Hello World" -> "hELLO wORLD"

        
#___________________________________________________________________________________

# Masala 1: Email tekshirish
# Berilgan string email formatida ekanligini tekshiring. Emailda "@" va "." belgisi bo'lishi kerak.

# Misol:

# python
# Copy code
# input: "example@domain.com"
# output: True

# input: "example@domaincom"
# output: False
# Masala 2: So'zlarni kapitalizatsiya qilish
# Berilgan stringdagi har bir so'zning bosh harfini katta qiling.

# Misol:

# python
# Copy code
# input: "hello world"
# output: "Hello World"
# Masala 3: URL shifrlash (URL encoding)
# Berilgan stringdagi bo'sh joylarni va maxsus belgilarni % bilan shifrlang.

# Misol:

# python
# Copy code
# input: "hello world!"
# output: "hello%20world%21"
# Masala 4: Eng uzun so'zni topish
# Berilgan stringdagi eng uzun so'zni aniqlang.

# Misol:

# python
# Copy code
# input: "The quick brown fox jumped over the lazy dog"
# output: "jumped"
# Masala 5: String ichida substringni qidirish
# Berilgan stringda ma'lum bir substring mavjudligini tekshiring.

# Misol:

# python
# Copy code
# input: ("hello world", "world")
# output: True

# input: ("hello world", "python")
# output: False
# Masala 6: Case insensitive qidirish
# Berilgan stringda ma'lum bir substringni qidirishda katta-kichik harf farqini inobatga olmasdan tekshiring.

# Misol:

# python
# Copy code
# input: ("Hello World", "hello")
# output: True
# Masala 7: Stringni palindrom ekanligini tekshirish
# Berilgan string palindrom ekanligini tekshiring. Bo'sh joylar va katta-kichik harflarni inobatga olmang.

# Misol:

# python
# Copy code
# input: "A man a plan a canal Panama"
# output: True
# Masala 8: Duplicate harflarni olib tashlash
# Berilgan stringdan barcha takroriy harflarni olib tashlang.

# Misol:

# python
# Copy code
# input: "hello"
# output: "helo"
# Masala 9: Stringni integerga aylantirish
# Berilgan string integerga aylantiring. Agar string integer bo'lmasa, 0 qaytaring.

# Misol:

# python
# Copy code
# input: "123"
# output: 123

# input: "abc"
# output: 0
# Masala 10: Stringdagi so'zlarni soniga qarab tartiblash
# Berilgan stringdagi so'zlarni uzunligiga qarab tartiblash.

# Misol:

# python
# Copy code
# input: "The quick brown fox"
# output: "The fox brown quick"
# Bu masalalarni yechish orqali siz string metodlarini chuqurroq o'rganishingiz mumkin. Har bir masalani yechishda Python string metodlaridan foydalaning va o'rganish jarayonini yanada samarali qiling.

# yechim kerak emas faqat masala shartini ber 
# ChatGPT
# Albatta, faqat masala shartlari quyida keltirilgan:

# Masala 1: Email tekshirish
# Berilgan string email formatida ekanligini tekshiring. Emailda "@" va "." belgisi bo'lishi kerak.

# Misol:

# python
# Copy code
# input: "example@domain.com"
# output: True

# input: "example@domaincom"
# output: False
# Masala 2: So'zlarni kapitalizatsiya qilish
# Berilgan stringdagi har bir so'zning bosh harfini katta qiling.

# Misol:

# python
# Copy code
# input: "hello world"
# output: "Hello World"
# Masala 3: URL shifrlash (URL encoding)
# Berilgan stringdagi bo'sh joylarni va maxsus belgilarni % bilan shifrlang.

# Misol:

# python
# Copy code
# input: "hello world!"
# output: "hello%20world%21"
# Masala 4: Eng uzun so'zni topish
# Berilgan stringdagi eng uzun so'zni aniqlang.

# Misol:

# python
# Copy code
# input: "The quick brown fox jumped over the lazy dog"
# output: "jumped"
# Masala 5: String ichida substringni qidirish
# Berilgan stringda ma'lum bir substring mavjudligini tekshiring.

# Misol:

# python
# Copy code
# input: ("hello world", "world")
# output: True

# input: ("hello world", "python")
# output: False
# Masala 6: Case insensitive qidirish
# Berilgan stringda ma'lum bir substringni qidirishda katta-kichik harf farqini inobatga olmasdan tekshiring.

# Misol:

# python
# Copy code
# input: ("Hello World", "hello")
# output: True
# Masala 7: Stringni palindrom ekanligini tekshirish
# Berilgan string palindrom ekanligini tekshiring. Bo'sh joylar va katta-kichik harflarni inobatga olmang.

# Misol:

# python
# Copy code
# input: "A man a plan a canal Panama"
# output: True
# Masala 8: Duplicate harflarni olib tashlash
# Berilgan stringdan barcha takroriy harflarni olib tashlang.

# Misol:

# python
# Copy code
# input: "hello"
# output: "helo"
# Masala 9: Stringni integerga aylantirish
# Berilgan string integerga aylantiring. Agar string integer bo'lmasa, 0 qaytaring.

# Misol:

# python
# Copy code
# input: "123"
# output: 123

# input: "abc"
# output: 0
# Masala 10: Stringdagi so'zlarni soniga qarab tartiblash
# Berilgan stringdagi so'zlarni uzunligiga qarab tartiblash.

# Misol:

# python
# Copy code
# input: "The quick brown fox"
# output: "The fox brown quick"