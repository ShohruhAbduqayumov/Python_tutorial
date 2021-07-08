# 20 yoshdan kattalarini chiqarish

shaxslar = [
    {
        "ism": "Shohruh",
        "yoshi": 29
    },
    {
        "ism": "Oybek",
        "yoshi": 19
    },
    {
        "ism": "Jahongir",
        "yoshi": 27
    },
    {
        "ism": "Bunyod",
        "yoshi": 18
    }
]
for shaxs in shaxslar:
    for key in shaxs:
        if key == "yoshi" and shaxs[key] > 20:
            print(shaxs)


A harfi bilan boshlanganlarini chiqarish

shaxslar = [
    {
        "ism": "Shohruh",
        "yoshi": 29
    },
    {
        "ism": "Oybek",
        "yoshi": 19
    },
    {
        "ism": "Aziz",
        "yoshi": 27
    },
    {
        "ism": "Abdulla",
        "yoshi": 18
    }
]
for shaxs in shaxslar:
    if shaxs["ism"][0] == "A":
        print(shaxs)


