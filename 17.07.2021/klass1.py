class Xodim:
    def __init__(self, ism, fam, yosh):
        self.ism = ism
        self.fam = fam
        self.yosh = yosh


s = Xodim("Shohruh", "Abduqayumov", 28)
a = Xodim("Oybek", "Narzullayev", 22)

print(s.__dict__)
print(a.__dict__)
print(s.ism, s.fam, s.yosh)
print(a.ism, a.fam, a.yosh)
