""" classda metodlar """


class Avtomobil:
    def __init__(self, rusumi):
        self.rusumi = rusumi

    def signal(self):
        print("Biiib!!!!")


malibu = Avtomobil("Malibu")
malibu.signal()


class Shaxs:
    def __init__(self, ism, fam):
        self.ism = ism
        self.fam = fam

    def tuliq_ism(self):
        return self.ism + ' ' + self.fam


sh1 = Shaxs("Oybek", "Narzullaev")
print(sh1.tuliq_ism())