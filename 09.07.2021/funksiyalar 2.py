""" return """

a = 2
b = 1


# shularni yig'indisni hisoblasin
def yigindi(a, b):
    return a + b


print(yigindi(a, b))

""" o'rta arifmetik """


def urta(a, b, c):
    return (a + b + c)/3


a = 2
b = 1
c = 3

urt = urta(a, b, c)

print(urt)


# 2 - masala
def f(x):
    if x == 0:
        return 0
    elif x % 2 == 0:
        return 1
    elif x % 2 == 1:
        return -1


x = int(input("x = "))
y = f(x)
print(y)


# 3 - masala. ikki sonning kattasini qaytarib beradigan funksiya tuzing
def katta(a, b):
    if a > b:
        return a
    else:
        return b


print(katta(3, 2))

sum = 0
for i in range(3):
    sum += i
    print(i)

print(i, sum)


# 4 - masala. berilgan sonni avval modulini topib so'ng ikkiga orttiriladigan qiymatini qaytaring


def modul(n):
    if n >= 0:
        return n
    else:
        return -n


def ikkilash(n):
    return 2 * n


def masala(n):
    m = modul(n)
    return ikkilash(m)


print(masala(-5))

# 5 - masala. 1) biringi juft toqligini topasiz. 2) ikkinchi toq bo'lsa 4 ga ko'pyatirb qaytarasiz
# juft bo'lsa ikkiga ko'paytirb qaytarasiz.
# 3) umumiy masala degan f-ya bu qolgan ikkisini chaqiradi


def jufttoq(n):
    if n % 2 == 0:
        return 0
    else:
        return 1


def amal(n, key):
    if key == 0:
        return n * 2
    else:
        return n * 4


def masala(n):
    k = jufttoq(n)
    return amal(n, k)


print(masala(2))