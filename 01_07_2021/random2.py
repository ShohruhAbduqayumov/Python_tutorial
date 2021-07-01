# import random
#
# while True:
#     kiritilganSon = int(input("son -> "))
#     tasodifiySon = random.randint(1, 10)
#     if kiritilganSon == tasodifiySon:
#         print("Yutdingiz")
#         break
#     else:
#         print("Dam oling")

import random

imkoniyat = 1
yutdimi = False

while imkoniyat <= 5:
    kiritilganSon = int(input("son -> "))
    tasodifiySon = random.randint(1, 10)
    if kiritilganSon == tasodifiySon:
        print("Yutdingiz")
        yutdimi = True
        break
    imkoniyat += 1

if not yutdimi:
    print("Yutqazdingiz")
