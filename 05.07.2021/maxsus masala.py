""" maxsus masala. 3x3 matritsa berilgan for yordamida ustunlarini satrga
  satrlarini ustunga almashtiring.
  masalan:
  """

b = [[[],[],[]],[[],[],[]],[[],[],[]]]
a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for i in range(3):
    for j in range(3):
        b[i][j] = a[j][i]
print(b)


""" 8-masala ikki o'lchovli mattrisanining juft elementlarini chiqaring"""
d = []
c = [[1,2],[3,4]]
for i in c:
    for j in i:
        if j % 2 == 0:
            d.append(j)

print(f"d = {d}")

""" 9-masala. ikki o'lchovli matritsaning toq elementlarini ikkiga ko'paytirib qo'ying
juft elementlarini ikkiga bo'lib qo'ying
"""

e = [[1,2],[3,4]]
print(e)
for i in range(2):
    for j in range(2):
        if e[i][j] % 2 == 0:
            e[i][j] = int(a[i][j] / 2)
        else:
            e[i][j] = e[i][j] * 2

print(e)

