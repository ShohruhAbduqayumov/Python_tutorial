# 1 - masala. Xodim class yaratasiz undan 5 ta obyekt olasiz
# Xodim klasida -> ismi, manzili, maoshi
# maoshi 2 mln dan kamlarini ismini chiqarasiz

class Xodim:
    def __init__(self, ism, manzili, maoshi):
        self.ism = ism
        self.manzili = manzili
        self.maoshi = maoshi


xodimlar = []

x1 = Xodim("Oybek", "G'allaorol", 2500000)
xodimlar.append(x1)
x2 = Xodim("Shohruh", "Jizzax", 3000000)
xodimlar.append(x2)
x3 = Xodim("Jahon", "Zarbdor", 2300000)
xodimlar.append(x3)
x4 = Xodim("Sunnat", "Paxtakor", 1800000)
xodimlar.append(x4)
x5 = Xodim("Ozoda", "Jizzax", 1500000)
xodimlar.append(x5)

for i in xodimlar:
    if i.maoshi < 2000000:
        print(i.ism)
