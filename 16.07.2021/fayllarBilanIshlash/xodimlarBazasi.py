import os

# 1. baza.txt faylini bor yo'qligini tekshirish
if not os.path.exists("baza.txt"):
    f = open("baza.txt", "x")

n = int(input("Xodimlar sonini kiriting: "))

f = open('baza.txt', 'a')

xodimlar = []
xodim = {
    "id": 0,
    "ism": '',
    "fam": '',
    "maosh": '',
    "manzil": ''
}

for i in range(n):
    print("Xodim ma'lumotlarini kiriting: ")
    print(f"{i + 1} - xodim")
    xodim['id'] = i + 1
    xodim["ism"] = input("ismi: ")
    xodim["fam"] = input("familiyasi: ")
    xodim["maosh"] = input("maoshi: ")
    xodim["manzil"] = input("manzili: ")
    temp = xodim.copy()
    xodimlar.append(temp)

f.write(str(xodimlar))
f.close()

# yangilash
print("Yangilamoqchi bo'lgan xodim ismini kiriting: ")
key = int(input("ismi: "))
f = open("baza.txt", 'r')
data = f.read().split('}, {')

for i in range(len(data)):

# ekranga chiqarish:
    f = open("baza.txt", 'r')
    data = f.read()
    data = data.split(', ')

for i in data:
    print(i)