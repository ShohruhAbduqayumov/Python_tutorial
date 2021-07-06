""" Matritsani diogonal bo'yicha chiqarish """

d = [[],[],[]]
c = [[1,2,3], [4,5,6], [7,8,9]]
for i in range(3):
    d[i] = c[i][i]

print(f"d = {d}")

""" kortej funksiyalari qo'llanilishi """

numbers = (1, 0, 4, 3, 2, 5, 6)

print(numbers.count(3))
print('--------------')

print(numbers.index(1))
print('--------------')

print(any(numbers))
print('--------------')

print(max(numbers))
print('--------------')

print(min(numbers))
print('--------------')

print(len(numbers))
print('--------------')

print(sorted(numbers))
print('--------------')

print(sum(numbers))

""" 2-topshiriq kortej tuziladi va eng katta va eng kichik elementlari yig'indisini va
  o'rta arifmetigini toping """

numbers = (1, 13, 4, 3, 2, -5, 6)

a = max(numbers)
b = min(numbers)
c = a + b
print(c)
print(sum(numbers) / len(numbers))

# maxsus usul bilan ishlash

i = 0
summa = 0
for number in numbers:
    i += 1
    summa += number

urta_arifmetik = summa / i
print(urta_arifmetik)

""" 3-topshiriq.  """

sonlar = (1, 2, 3, 4, 5)
a = []
b = []
x = int(len(sonlar))
for i in range(x):
    if i%2==1:
        a.append(sonlar[i])
print(a)
for i in range(x):
    if i%2==0:
        b.append(sonlar[i])
print(b)

# 2-usul
# birinchi avval juft o'rindagilarini keyin toq o'rindagilarini chiqaring
a = (1, 4, 10, 6, 7) # e'lon qilish
juft = [] # juft degan ro'yhat
toq = [] # toq degan ro'yhat
for i in range(len(a)):
    if (i + 1) % 2 == 0:
        juft.append(a[i])
    else:
        toq.append(a[i])
print(juft)
print(toq)

