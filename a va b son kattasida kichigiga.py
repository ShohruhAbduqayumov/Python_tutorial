a = int(input("a="))
b = int(input("b="))

if a > b:
    for i in range(b,a+1):
        print(i, end=";")
else:
    for i in range(b, a-1, -1):
        print(i, end=";")