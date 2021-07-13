"""xatolar bilan ishlash"""

# SyntaxError
print("salom')

# IdentionError
if a == 0:
print(1)

# NameError
try:
    name = "Shohruh"
    print(fulName)
except:
    print("NameError")

# valueError
try:
    x = "5.8"
    int(x)
except:
    print("xato -> ValueError")

""" 
try - > urinib ko'rmoq
except -> istisno qilmoq
"""

""" bir necha istisnolar """
try:
    # Nameerror
    ism = "Shohruh"
    print(ism)

    # ValueError
    i = '1.0026'
    int(i)
except NameError:
    print("ism o'zgaruvchisi nomida xato")
except ValueError:
    print("qiymatda xatolik")

""" else -> kodingiz to'g'ri ishlaganda chiqadigan natija """

try:
    print("Inson holati", end=" ")
except:
    print("Inson kasal")
else:
    print("Soppa - sog'")

""" finally -> try except jarayoni tagagundan so'ng ishlatiladi"""
y = 0
try:
    y = 0

    print("salom")
except:
    y += 1
    print("try dagi nimadur xato")
finally:
    if y == 0:
        print("dasturda xato yo'q")
    else:
        print("dasturda xato bor")



""" xato xabarini ko'rish """

import sys
try:
    x = 20 / 0
except:
    print(sys.exc_info())


