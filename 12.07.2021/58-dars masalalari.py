"""# 1-masala

n = int(input("n->"))

def kvadratcha(parametr):
    for i in range(parametr):
        print(n * '*')

kvadratcha(n)

# 2-usul

n = int(input("n->"))

def nYulduzcha(parametr):
    print((n * '*' + '\n') * n)

kvadratcha(n)

"""

"""
# 2-masala

n = int(input("n = "))

def buluvchilari(a):
    s = str('')
    for i in range(1,a+1):
        if a % i == 0:
            s += str(i) + ' '
    print(s)

buluvchilari(n)

# 2-usul

n = int(input("n = "))

def buluvchilari(a):
    for i in range(1,a+1):
        if a % i == 0:
            print(i, end=" ")

buluvchilari(n)

"""

"""
# 3 - masala. 200 ga teng va undan kichik sonlar uchun
n = int(input("n = "))

def rim(a):
    txt = ''
    if a // 100 > 0:
        k = a // 100
        txt += k * 'C'
    if a // 10 % 10 >= 0:
        k = a // 10 % 10
        if k <= 3:
            txt += k * 'X'
        elif k == 4:
            txt += 'XL'
        elif k >= 5 and k < 9:
            txt += 'L' + (k - 5) * 'X'
        elif k == 9:
            txt += 'XC'
    if a % 10 > 0:
        v = a % 10
        if v < 4:
            txt += 'I' * v
        elif v == 4:
            txt += 'IV'
        elif v < 9 and v > 4:
            txt += "V" + (v - 5) * "I"
        elif v == 9:
            txt += "IX"
    print(txt)


rim(n)

"""
"""
# 4-masala

n = int(input("n = "))

def xona_yigindi(a):
    yigindi = 0
    for i in range(len(str(a))):
        yigindi += a // (10 ** i) % 10
    print(yigindi)

xona_yigindi(n)

# 2-usul
n = int(input("n = "))

def xona_yigindi(a):
    summa = 0
    a = str(a)
    for i in a:
        summa += int(i)
    print(summa)

xona_yigindi(n)

"""
"""
# 6-masala

n = int(input("n = "))

def xona_soni(a):
    s = 0
    a = str(a)
    for i in a:
        s += 1
    print(s)

xona_soni(n)

# 2-usul

n = int(input("n = "))

def xona_soni1(a):
    return len(str(a))

print(xona_soni1(n))

# 3-usul

n = int(input("n = "))

def xona_soni1(a):
    xonalar = 0
    d = 0
    while 10 ** d <= a: # 1 <= 125; 10 <= 125;
        xonalar += 1
        d += 1

    return xonalar


print(xona_soni1(n))
"""

"""
# 5 - masala.
ballar = []

for i in range(5):
    k = int(input(f"{i + 1} - hakam -> "))
    ballar.append(k)

eng_katta = max(ballar)
eng_kichik = min(ballar)

def urt(a):
    summa = 0
    for i in a:
        if i == eng_katta or i == eng_kichik:
            continue
        else:
            summa += i
    return summa / (len(a) - 2)


print(f"{eng_kichik} {eng_katta}")
print(f"{urt(ballar)}")

"""