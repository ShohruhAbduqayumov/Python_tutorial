# 5 - masala
# raqamini kiritasiz va shu indeksgacha fibonachi sonlar ro'yhatini tuzasiz
# fibonachi sonlari -> 1, 1, 2, 3, 5, 8, 13, 21 ...

indeks = int(input("=>"))

a = []

for i in range(indeks + 1):
    if i == 0 or i == 1:
        a.append(1)
    else:
        a.append(a[i - 1] + a[i - 2])

print(a)