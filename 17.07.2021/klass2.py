class Avtomobil:
    def __init__(self, rusumi, yili, rangi, firmasi):
        self.rusumi = rusumi,
        self.yili = yili,
        self.rangi = rangi,
        self.firmasi = firmasi


malibu = Avtomobil("Malibu", 2022, "qora", "Chevrolet")
lacetti = Avtomobil("lacetti", 2020, "oq", "Chevrolet")

print(malibu.rusumi, malibu.rangi)
print(malibu.__dict__)
