""" 1-masala """

daraja2 = lambda a: a ** 2

print(daraja2(10))

""" 2-masala """

urta_arifmetik = lambda a, b, c, d: (a + b + c + d) / 4

print(urta_arifmetik(1, 2, 3, 4))


""" 3-masala. Ixtiyoriy sonlar darajasini chiqarish"""

def kvadrat(n):
    return lambda a: a ** n

son = kvadrat(5)

print(son(2))
print(kvadrat(5)(2))

""" aylananing uzunligini kiritish orqali funksiyani ichida lambdani qo'llab doira yuzini chiqaring"""

# l = 2 * pi * R
# S = pi * (R ** 2)

import math

def doira(l):
    return lambda pi: pi * ((l / 2 * pi) ** 2)

x = doira(10)
print(x(3.14))


""" Paralalepeped hajmini chiqarish """

def paralelopiped(a, b):
    return lambda c: a * b * c

x = paralelopiped(2, 3)
print(x(4))

""" ikki sonning yig'indisini n - darajasini chiqaring """

def yig_dar(a, b):
    return lambda n: (a + b) ** n

x = int(input("x= "))
y = int(input("y= "))
z = int(input("z= "))

k = yig_dar(x, y)
print(k(z))



""" ismingizni input qilasiz uni n marta chiqaring """

def ism(a):
    return lambda n: (a + ' ') * n

h = input("ismingizni kiriting-> ")
n = int(input("necha marta chiqarsin-> "))

n_ta_ism = ism(h)
print(n_ta_ism(n))
