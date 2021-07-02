# 2-masala. Butun sonlardan iborat ro'yhat berilgan juftlarini ekranga chiqaring

sonlar = [1,2,3,4,5,6]

for son in sonlar:
    if son % 2 == 0:
        print(son)

# 3-masala. Butun sonlardan iborat ro'yhat berilgan. Oldin juftlarini
# keyin toqlarini o'zlashtirib konsolga chiqaring

sonlar = [1,2,3,4,5,6]
sonlar1 = []

#birinchi juftlarini o'zlashtiramiz
for son in sonlar:
    if son % 2 == 0:
        sonlar1.append(son)

print(sonlar1)

#ikkinchi toqlarini o'zlashtiramiz
for son in sonlar:
    if son % 2 == 1:
        sonlar1.append(son)

print(sonlar1)

# 4-masala.

