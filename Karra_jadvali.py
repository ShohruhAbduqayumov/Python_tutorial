son = int(input("son kiriting: "))
for i in range(1,10):
    while True:
        print(son, "*", i, "=")
        natija = int(input(""))
        if natija == son * i:
            print("To'g'ri keyingisi")
            break
        else:
            print("Xato qayta kiriting")