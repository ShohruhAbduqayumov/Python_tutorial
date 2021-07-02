# maxsus masala 1. ro'yhat berilgan. input qilingan yangi o'zgaruvchini input qilingan
# yangi indeksga insert metodisiz joylashtiring
# masalan:
# sonlar = [1, 2, 3, 4] bo'lsin
# input -> element = 10, index = 2
# javobi ikkinchi indeksga 10 degan son kiritilsin
# sonlar = [1, 2, 10, 3, 4]
"""
# insert funksiyasi bilan

sonlar = [1,2,3,4]

element = int(input("element -> "))
index = int(input("index -> "))

sonlar.insert(index,element)

print(f"sonlar = {sonlar}")

"""
# insert funksiyasisiz ishlatish

uquvchilar = ['Azamat','Shohruh','Jahongir','Shoxjahon','Baxtiyor']

name = input("name=")
index = int(input("index="))

uquvchilar1 = uquvchilar.copy()
uquvchilar[index] = name

uquvchilar.append(uquvchilar1[index])
print(uquvchilar)
