#  1 - masala

from math import factorial as f
def myFunction(n, k):
    return f(n) / (f(k) * f(n - k))

print(myFunction(6, 4))


# 2 - masala

def kv(n):
    for i in range(1,n):
        if i ** 2 < n:
            print(i)
n = int(input("n="))

kv(n)


# 2-masala 2-usul

n = int(input("n="))

def kv2(n):
    qiymat  = []
    for i in range(1,n):
        if i ** 2 < n:
            qiymat.append(i)
    return qiymat

print(kv2(n))


# 3-masala

n = int(input("n->"))

def n_chiziq(parametr):
    txt = ''
    for i in range(parametr):
        txt += '-'
    print(txt)

n_chiziq(n)

# 3-masala 2-usul

n = int(input("n->"))

def n_chiziq(parametr):
   print('-' * n)

n_chiziq(n)

