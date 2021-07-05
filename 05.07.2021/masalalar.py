""" 1 - masala. 10 raqamini indeksi orqali print qiling """

numbersList = [[1, 2, 3, 4], [0, [1, 2, [4, 5, [10, 11]], 4], 5], 12]
print(numbersList[1][1][2][2][0])

""" 2- masala """
list = [[1,2,3],[4,5,6],[7,8,9]]
print(list[1][1])

""" 3-masala"""
matrix1 = [[1,2],[3,4]]
matrix2 = [[5,6],[7,8]]
matrix = [[matrix1[0][0]+matrix2[0][0],matrix1[0][1]+matrix2[0][1]],[matrix1[1][0]+matrix2[1][0],matrix1[1][1]+matrix2[1][1]]]
print(matrix)

# for bilan ishlanishi

B = [[[],[]],[[],[]]]
for i in range(2):
    for j in range(2):
        B[i][j] = matrix1[i][j] + matrix2[i][j]
print(B)

""" 4-masala """

matrix_3x3 = [[1,2,3],[4,5,6],[7,8,9]]
print(matrix_3x3)

# for bilan ishlanishi

A = [[[],[],[]],[[],[],[]],[[],[],[]]]
for i in range(3):
    for j in range(3):
        A[i][j] = int(input(f"A[{i}][{j}] = "))

print(A)

""" 5-masala 3x3 matrisa har bir elementini alohida qatorga chiqaring """

mat = [[1,2,3],[4,5,6],[7,8,9]]
for i in mat:
    for j in i:
        print(j)

""" 6-masala. 2x2 ro'yhat berilgan ana shu ro'yhatni bir o'lchovli ro'yhatga o'zlashtiring
 masalan: [[1,2],[3,4]] -> [1,2,3,4] """

a = [[1,2],[3,4]]
print(a[0]+a[1])

# for bilan ishlash

c = []
a = [[1,2],[3,4]]
for i in a:
    for j in i:
        c.append(j)
print(c)

""" 7-masala b ni generatsiya qiling """

M = [[1,2,3],[4,5,6],[7,8,9]]
N = [M[0][0],M[0][1],M[0][2],M[1][2],M[2][2],M[2][1],M[2][0],M[1][0],M[1][1]]
print(N)

""" massiv elementini o'chirish """
from array import *

array1 = array('i', [10,20,30,40,50])
array1.remove(40)
for x in array1:
    print(x)
