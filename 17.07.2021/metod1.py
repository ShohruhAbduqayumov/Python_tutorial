class Shaxs:
    def __init__(self, ism, fam, shahri, mahallasi):
        self.ism = ism
        self.fam = fam
        self.shahri = shahri
        self.mahallasi = mahallasi

    def tuliq_ism(self):
        return self.ism + ' ' + self.fam

    def manzil(self):
        return self.shahri + ' shahri ' + self.mahallasi + ' MFY;'


sh1 = Shaxs("Shohruh", "Abduqayumov", "Jizzax", "Olmazor")
print(sh1.tuliq_ism(), sh1.manzil())
