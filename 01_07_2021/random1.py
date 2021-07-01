# 1 dan 10 gacha bo'lgan butun son kiriting va randint bilan tuzulgan
# generatsiya qilingan son bilan solishtiring

import random

kiritilganSon = int(input("son -> "))
tasodifiySon = random.randint(1, 10)

if kiritilganSon == tasodifiySon:
    print(tasodifiySon)
    print("Yutdingiz")
else:
    print(tasodifiySon)
    print("Dam oling")