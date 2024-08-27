# def dct(a:str):
#     d = {}
#     key=''
#     for i in a:
#         if i not in d:
#          d[i] = 1
#         else:
#            d[i] = d[i] + 1
#     print(d)


# dct(input(">>> "))



# for i in range(100, 1000):
#     son = str(i)
#     for raqam in set(son):
#         if son.count(raqam) == 2:
#             print(son)


# def son():
#     for i in range(1000,10000):
#         a = str(i)
#         s=''.join(set(a))
#         if len(s) == len(a):
#             print(s)
#son()


# son = input("Son kiriting: ")
# n=len(str(son))
# for i in son:
#     a=str(i)+"0" * (n-1)
#     if len(a)<2:
#         print(a)
#     else :
#         print(a,end="+")
#     n-=1

#SONNING CHAP TARAFIGA SON QO'YISH

# a = int(input("k>>> "))
# b = int(input("N>>> "))
# s=b
# while s != 0:
#     a *= 10
#     s //= 10
# print(a+b)

#DICT QO'SHISH

# def dct(d:dict,t:dict):
#     new={}
#     for i in set(d.keys()).union(set(t.keys())):
#         v1 = d.get(i,0)
#         v2 = t.get(i,0)
#         new[i] = v1+v2    
#     return new
# d={'a':100,'b':200,'c':300}
# t={'a':300,'b':200,'d':400}
# g=dct(d,t)
# print(g)


