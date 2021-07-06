# maxsus masala 2

a = (1, 2, 3, 4, 5, 6, 7, 8)
b = list(a)
c = []
for i in range(len(b)):
    c.append(b[0])
    if b[0] == b[-1]:
        break
    c.append(b[-1])
    b.pop(0)
    b.pop(-1)
    if not b:
        break
a = tuple(c)
print(a)

# 2-usul

a = (1, 2, 3, 4, 5, 6, 7, 8)
i = 0
b = list(a)
c = []
while i < (len(a) // 2):
    if i == 0:
        c.append(b[0])
    else:
        c.append(b[-i])
        c.append(b[i])
    i += 1
else:
    c.append(b[i])
print(c)

# 3-usul

a=(1,2,3,4,5,6,7,8)
b=list(a)
mk=[]
k=len(b)-1
for i in range(len(b)//2):
    mk.append(b[i])
    mk.append(b[k])
    k-=1
print(mk)