#LIST 
#1-m

# a = ''.join(['j','a','v','a'])
# print(a)

#2-m

# a = [[1,2],[0,0,2],[7,0],[2,1]]
# b = []
# print(max(a, key=lambda x: sum(x)))

#3-m

# a = ['alik','faund','ation','78','arsenal']
# print(max(a, key=lambda x:len(x)))

#4-m

# a = [[],['salom'],[],[],[2,3,4],[],[]]
# for i in a[::-1]:
#     if i == []:
#         a.remove(i)
# print(a)

#TUPLE

#1-m

# a = ['p','q']
# n = int(input(">>> "))
# b = []
# r = 1
# while r < n:
#     for i in a:
#         b.append(i + str(r))
#     r+=1
# print(b)

#2-m

# a = ((1,2,3),(4,5),(8,9,10,11))
# b = list(a)
# b.remove(max(b, key=lambda x: len(x)))
# t = tuple(j for i in b for j in i)
# print(t)


data = [
    {"full_name":"Eugene Elsmor","company":"Kazu","position":"Electrical Engineer","salary":"$4440.86"},
    {"full_name":"Joni Stredder","company":"JumpXS","position":"Environmental Tech","salary":"$870.05"},
    {"full_name":"Terri-jo Fulham","company":"Tagchat","position":"Assistant Media Planner","salary":"$1992.55"},
    {"full_name":"Priscilla Pandya","company":"Youopia","position":"Help Desk Operator","salary":"$3715.95"},
    {"full_name":"Wolfy Swanborough","company":"Topiclounge","position":"Recruiter","salary":"$1045.61"},
    {"full_name":"Raleigh Ratter","company":"Zoozzy","position":"Graphic Designer","salary":"$602.41"},
    {"full_name":"Anastasia Winward","company":"Avaveo","position":"Cost Accountant","salary":"$3641.42"},
    {"full_name":"Dorry Vasyunichev","company":"Fivebridge","position":"Junior Executive","salary":"$2035.05"},
    {"full_name":"Richy Cleft","company":"Jamia","position":"Sales Associate","salary":"$912.98"},
    {"full_name":"Zack Record","company":"Oyonder","position":"Social Worker","salary":"$2492.23"},
    {"full_name":"Lissy Newns","company":"Riffwire","position":"Developer II","salary":"$1177.79"},
    {"full_name":"Audrye Churchyard","company":"Photospace","position":"Environmental Tech","salary":"$4125.83"},
    {"full_name":"Timothy Seligson","company":"Riffpath","position":"Compensation Analyst","salary":"$1271.94"},
    {"full_name":"Brandie Rogeon","company":"Riffpath","position":"Analyst Programmer","salary":"$1911.09"},
    {"full_name":"Dane Rugg","company":"Twimm","position":"Associate Professor","salary":"$2200.72"},
    {"full_name":"Mick Jeduch","company":"Realblab","position":"Executive Secretary","salary":"$1154.20"},
    {"full_name":"Rowland Christofol","company":"Mycat","position":"Senior Cost Accountant","salary":"$1119.94"},
    {"full_name":"Sibella Abrahams","company":"Minyx","position":"Internal Auditor","salary":"$4023.25"},
    {"full_name":"Layne Thomel","company":"Centimia","position":"Research Associate","salary":"$4073.17"},
    {"full_name":"Demetris Clemenzi","company":"Tagopia","position":"Human Resources Manager","salary":"$1530.37"},
    {"full_name":"Kerstin Devon","company":"Katz","position":"Senior Quality Engineer","salary":"$1305.61"},
    {"full_name":"Brandon Burgwyn","company":"Mydeo","position":"Physical Therapy Assistant","salary":"$1325.58"},
    {"full_name":"Dyana Crosby","company":"Riffpath","position":"Payment Adjustment Coordinator","salary":"$1501.54"},
    {"full_name":"Harald Voller","company":"Riffpedia","position":"Accountant I","salary":"$4397.60"},
    {"full_name":"Nollie Phipard-Shears","company":"Aimbo","position":"Legal Assistant","salary":"$3172.57"},
    {"full_name":"Gaynor Dannohl","company":"Riffpath","position":"Administrative Assistant II","salary":"$3035.89"},
    {"full_name":"Tome Bensen","company":"Yamia","position":"Assistant Professor","salary":"$3677.10"},
    {"full_name":"Jessey Anshell","company":"Bubblemix","position":"Registered Nurse","salary":"$2782.66"},
    {"full_name":"Valentijn Melbury","company":"Bluejam","position":"Statistician I","salary":"$1308.43"},
    {"full_name":"Rochelle Andrejevic","company":"Riffpath","position":"VP Product Management","salary":"$1734.61"}
]


# 1 - masala: Human Resources Manager bo'limida nechta odam ishlashini hisoblang

# 2 - "Riffpath" kompaniyasida ishlaydigan barcha 
# hodimlarga qancha maosh to'lanishini hisoblang 
# (maosh olida $ belgisi bor e'tiborli bo'ling)

# 3 - Ismi "K" dan boshlanadigan hodimlarni oyligini 2-karra oshiring

# 4 - barcha "full_name" keylari ni o'rniga "FIO" ga almashtiring 
# value lar o'chib ketmasin

# 5 - masala "position" keyning "valuesida" -> "senior" yoki "junior"
# satri bor barcha hodimlarni o'chirib tashlang

# 6 - masala "Assistant" lar soni nechtaligini hisoblang

# 7 - masala Barcha "Assistant" larni "Junior" pazitsiyaga o'tqazing
# misol -> "Assistant Professor" -> "Junior Professor"


#1-m
# c=0
# for i in data:
#     if i['position'] == 'Human Resources Manager':
#         print(i)
#         c += 1
# print(c)

#2-m
# c = 0
# a = []
# for i in data:
#     if i['company'] == 'Riffpath':
#         a.append(i['salary'][1:])
# print(f"${sum([float(i) for i in a])}")

#3-m

# for i in data:
#     if i['full_name'][:1] == 'K':
#         print(f"oylik ${float(i['salary'][1:]) * 2}\n{i}")

#4-m

# for i in data:
#     i["FIO"] = i.pop("full_name")
# print(*data, sep="\n")    

#5-m
#      
# for i in data:
#     if 'Senior' in i['position'] or 'Junior' in i["position"]:
#         data.remove(i)
# print(*data, sep="\n")

#6-m

# count=0
# for i in data:
#     if 'Assistant' in i['position']:
#         print(i, end="\n")
#         count+=1
# print(count)

#7-m

# for i in data:
#     if 'Assistant' in i['position']:
#         i["position"] = i["position"].replace("Assistant","Junior")
# print(*data, sep="\n")


# a = ['osh','somsa','manti','shashlik','norin']
# b = {'somsa':12000,'osh':25000,'norin':35000}

# for taom in b:
#     if taom in a:
#         print(f"{taom.title()} {b[taom]} so'm")
# for i in a:
#     if i not in b:
#         print(f"{i} bu taomlar yo'q ekan")
