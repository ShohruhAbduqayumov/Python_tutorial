""" maxsusroq masala """

import random

a = []

for i in range(10):
    b = random.randint(1,10)
    a.append((b))
print(a)
a = set(a)

print(a)


""" maxsusroq masala 2 """
# matematika, informatika, fizika fanlaridan olimpiada bo'ldi. Olimpiadalar ketma ket bo'ldi
# olimpiadaga kirgan o'quvchilar ro'yhatini chiqaring

matematika = ["Shohruh","Jahongir","Begzod","Yorqin"]
fizika = ["Bunyod", "Jahongir", "Oybek","Shohruh"]
informatika = ["Oybek","Shohruh","Abbos","Bunyod"]

olimpiada = matematika + informatika + fizika
olimpiada = set(olimpiada)

print(olimpiada)

# qaysi fandan nechta borganligi

a = matematika + informatika
a = set(a)
a = len(a)
print(a)

b = matematika + fizika
b = set(b)
b = len(b)
print(b)

c = informatika + fizika
c = set(c)
c = len(c)
print(c)


""" maxsus masala """
import random as rd

A = []
B = []
C = []
# A va b to'plamlarni birlashmasini olib C to'plam bilan kesishmasini olasiz

for i in range(10):
    k = rd.randint(1, 10)
    A.append(k)

for i in range(10):
    k = rd.randint(1, 10)
    B.append(k)

for i in range(10):
    k = rd.randint(1, 10)
    C.append(k)

print(A)
print(B)
AUB = set(A + B)
print(AUB)

AUB = list(AUB)
C = set(C)
print(C)

D = []

for i in C:
    if i in AUB:
        D.append(i)

D = set(D)
print(D)


# 2-usul
import random as rd

A = []
B = []
C = []
# A va b to'plamlarni birlashmasini olib C to'plam bilan kesishmasini olasiz

for i in range(10):
    A.append(rd.randint(1, 10))
    B.append(rd.randint(1, 10))
    C.append(rd.randint(1, 10))


print(A)
print(B)
AUB = set(A + B)
print(AUB)

AUB = list(AUB)
C = set(C)
print(C)

D = []

for i in C:
    if i in AUB:
        D.append(i)

D = set(D)
print(D)