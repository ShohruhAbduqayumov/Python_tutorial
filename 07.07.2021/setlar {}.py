""" set ni yaratish """
# 1. gulli qavslar bilan
numbers = {1, 2, 3, 4, 5, 6}
print(type(numbers))

# 2. set() kosntruktori bilan
numbers = set([1, 2, 3, 4, 5]) # listni setga aylantirish
print(numbers)
print(type(numbers))

numbers = set((1, 2, 3, 4))
print(numbers)

""" elementlariga murojaat """
# Diqqat: setda indeks yo'q!!!
# setni listga aylantirish:
numbers = {1, 2, 3, 4, 5, 6}
numbers = list(numbers) # endi numbers list ga aylandi
print(numbers)
print(numbers[0])


""" setni barcha elementlarini ko'rish """
numbers = {1, 2, 3, 4, 5, 6}
print(numbers) # shunchaki setni o'zini print qilish
for i in numbers:
    print(i)


""" setda bir xil elementlar bo'lmadi """
fruits = {"apple", "orange", "banana", "apple"}
print(fruits)
# xulosa: set da bir xil element bo'lmaydi!


""" setda tarib muhimmas """
fruits = {"apple", "orange", "banana", "apple"}
fruits1 = {"orange", "apple", "banana"}
print(fruits1 == fruits)


""" element qo'shish """
mevalar = {"Olma", "Anor"}

# add funksiyasi bilan uning parametri mavjud bo'lishi shart! -> .metod(parametr)

mevalar.add("Shaftoli")
print(mevalar)
# set.method(parametr)

# update funksiyasi bilan set.update(*element)
mevalar.update(["Gilos", "Olxori"])
print(mevalar)


""" elementni o'chirish:"""
# remove
fruits = {"apple", "orange", "banana", "Cherry"}
fruits.remove("banana")
print(fruits)

# pop
fruits.pop()
print(fruits)

# clear -> tozalash
fruits = {"apple", "orange", "banana", "Cherry"}
fruits.clear() # bu bo'sh qiladi

print(fruits)

# del -> bu birato'la setni o'zini xotiradan o'chiradi
fruits = {"apple", "orange", "banana", "Cherry"}

del fruits
# print(fruits)

""" copy() parametri yo'q """

mevalar1 = {"Olma", "Anor"}

mevalar2 = mevalar1.copy()

print(f"{mevalar1} {mevalar2} ")

# nusxalashni o'zlashtirish amali bilan ham bajarsa bo'ladi

mevalar3 = mevalar1
mevalar1.clear()
print(mevalar3) # bu o'chib ketadi chunki bu o'zlashtirishdan hosil bo'lgan
print(mevalar2) # bu o'chmaydi chunki bu nusxalangan

""" difference() parametri bor u set qabul qiladi"""
mevalar1 = {"Olma", "Anor", "Olcha"}
mevalar2 = {"Apelsin", "Anor", "Ananas"}

print(mevalar1.difference(mevalar2)) # mevalar1 ni mevalar2 dan farqi

""" difference_update() parametr bor """
mevalar1 = {"Olma", "Anor", "Olcha"}
mevalar2 = {"Apelsin", "Anor", "Ananas"}

mevalar1.difference_update(mevalar2) # mevalar1 ni mevalar2 dan farqini o'ziga o'zlashtiradi
print(mevalar1)

""" intersection() kesishma ikkisida ham borlarini oladi """
mevalar1 = {"Olma", "Anor", "Olcha"}
mevalar2 = {"Apelsin", "Anor", "Ananas"}

print(mevalar1.intersection(mevalar2))

""" intersection_update ikkisida ham borlarini o'ziga o'zlashtiradi"""
mevalar1 = {"Olma", "Anor", "Olcha"}
mevalar2 = {"Apelsin", "Anor", "Ananas"}

mevalar1.intersection_update(mevalar2)
print(mevalar1)

""" isdisjoin() bu agar bitta setni ikkinchi setda bir xil elementi
    bo'lmasa True bo'lsa False qaytaradi"""
mevalar1 = {"Olma", "Anor", "Olcha"}
mevalar2 = {"Apelsin", "Anor", "Ananas"}

print(mevalar1.isdisjoint(mevalar2)) # hozirgi holarda False chunki ikkisida ham anor bor

""" issubset() -> set1.issubset(set2) - agar set2 ichida set1 bo'lsa True aks holsa False """
mevalar1 = {"Olma", "Anor", "Olcha", "Ananas"}
mevalar2 = {"Anor", "Olma"}

print(mevalar2.issubset(mevalar1))

""" issuperset() -> set1.issuperset(set2) agar set1 ni ichida set2 bo'lsa True aks holda False """
mevalar1 = {"Olma", "Anor", "Olcha", "Ananas"}
mevalar2 = {"Anor", "Olma"}

print(mevalar2.issuperset(mevalar1)) # hozirgi holatda False

""" symmetric_difference() set3 = set1.symmetric_difference(set2) set1 va set2 dagi bir xil
    elementlarini olib tashlab qolganlarini set3 ga o'zlashtiradi"""

mevalar1 = {"Olma", "Anor", "Olcha", "Ananas"}
mevalar2 = {"Anor", "Olma", "Apelsin", "Mandarin"}

mevalar3 = mevalar1.symmetric_difference(mevalar2)
print(mevalar3)

""" symmetric_difference_update() set1.symmetric_difference(set2) set1 va set2 dagi bir xil
    elementlarini olib tashlab qolganlarini set1 o'ziga o'zlashtiradi"""

mevalar1 = {"Olma", "Anor", "Olcha", "Ananas"}
mevalar2 = {"Anor", "Olma", "Apelsin", "Mandarin"}

mevalar1.symmetric_difference_update(mevalar2)
print(mevalar1)

""" union -> set1.union(set2) -> set1 va set2 ni birlashmasi"""
mevalar1 = {"Olma", "Anor", "Olcha", "Ananas"}
mevalar2 = {"Anor", "Olma", "Apelsin", "Mandarin"}

mevalar3 = mevalar1.union(mevalar2)

print(mevalar3)