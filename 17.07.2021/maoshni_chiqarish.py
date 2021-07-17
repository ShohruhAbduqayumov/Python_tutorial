class Xodim:
    def __init__(self, ism, manzili, maoshi):
        self.ism = ism
        self.manzili = manzili
        self.maoshi = maoshi

    def gap(self):
        return f"Mening ismim {self.ism} maoshim {self.maoshi}"


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
    print(i.gap())
