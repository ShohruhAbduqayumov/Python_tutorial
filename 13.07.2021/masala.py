# ism = input("ismingizni kiritng - > ")
# y = 1
# try:
#     print("salom" + ' ' + ism)
# except:
#     print("try dagi nimadur xato")
# finally:
#     if y == 1:
#         print("dasturda xato yo'q")
#     else:
#         print("dasturda xato bor")

# try:
#     n = int(input("n = "))
#
#     if n < 0:
#         raise Exception()
#
# except:
#     print("xato yo'q")
#
# else:
#     print("xato")

#
# """ xato xabarini ko'rish """
#
# import sys
# try:
#     x = 20 / 0
# except:
#     print(sys.exc_info())

# 3-masala.

import sys

try:
    n = int(input("n = "))
    if n % 2 == 0:
        raise Exception("siz juft son kiritdingiz")
except:
    print(sys.exc_info()[1])
else:
    print("xato yo'q")
finally:
    print("dastur tugadi")
