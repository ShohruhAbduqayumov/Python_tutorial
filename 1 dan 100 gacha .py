i = 1
for i in range(1,100):
    if i % 10 <= 5 and i // 10 > 0:
        continue
    print(i, end=";")