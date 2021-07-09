""" ro'yhat argument sifatida """


def uquvchilar(x):
    for i in x:
        print(i)


uquvchi = []
k = int(input("o'quvchilar sonini kiriting: "))

for i in range(k):
    ism = input(f"{i + 1} - o'quvchi ismi: ")
    uquvchi.append(ism)

uquvchilar(uquvchi)

""" o'rta arifmetik qaytarish """

a = 1
b = 2
c = 3

def urtaArifmetik(a,b,c):
    return (a + b +c) / 3

print(urtaArifmetik(a,b,c))

""" sistema """

def sistema(x):
    if x == 0:
        return 0
    elif x % 2 == 0:
        return 1
    else:
        return -1

x = int(input("x= "))

print(sistema(x))

""" 3-masala ikki sonning kattasini qaytarib beradigan funksiya"""

def katta(x, y):
    if x > y:
        return x
    else:
        return y

x = int(input("x= "))
y = int(input("y= "))

print(katta(x,y))

""" 4-masala 1-juft toqligini topasiz. 2-toq bo'sa 4 ga ko'payganini, juft bo'lsa 2 ga ko'payganini
qaytarasiz. 3- umumiy masala degan f-ya qolgan ikkisini chiqaradi """

def juftToq(n):
    if n % 2 == 0:
        return 0
    else:
        return 1


def amal(n, key):
    if key == 0:
        return 2 * n
    else:
        return 4 * n


def masala(n):
    key = juftToq(n)
    return amal(n, key)

print(masala(3))


""" masala """
def powerA3(n):
    return n ** 3

A = 1.1
B = 2.2
C = 3.3

D = 1
E = 2
print(powerA3(A))
print(powerA3(B))
print(powerA3(C))
print(powerA3(D))
print(powerA3(E))

