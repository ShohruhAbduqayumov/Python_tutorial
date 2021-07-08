# """ 1-masala lug'at hosil qilish"""
#
# uqituvchi = {
#     "ismi": "Shohruh",
#     "yoshi": 29,
#     "manzili": "Olmazor MFY"
# }
# print(uqituvchi)

# talaba = {
#     "ism": "SHohruh",
#     "yoshi": 29
# }
# yil = int(input("necha yil o'tdi -> "))
# talaba["yoshi"] = talaba["yoshi"] + yil
# print(talaba)

# shaxs = {
#     "ism": "Shohruh",
#     "yoshi": 10,
#     "o'quvchi": True
# }
# yil = int(input("yil - > "))
# shaxs["yoshi"] = shaxs["yoshi"] + yil
# if shaxs["yoshi"] > 19:
#     shaxs["o'quvchi"] = False
# print(shaxs)
#
# print("---------------")
#
# shaxs = {
#     "ism": "Shohruh",
#     "yoshi": 10,
#     "o'quvchi": True
# }
# yil = int(input("yil - > "))
# shaxs["yoshi"] = shaxs["yoshi"] + yil
# if shaxs["yoshi"] > 18:
#     shaxs.pop("o'quvchi")
# print(shaxs)

""" masala yoshi degan key bormi yo'qmi """
talaba = {
    "ism": "SHohruh",
    "yoshi": 29
}
if "yoshi" in talaba:
    print("Ha bor")
else:
    print("Yo'q")


# ikkinchi usul

talaba = {
    "ism": "SHohruh",
    "yoshi": 29
}
for i in talaba:
    if i == "yosh":
        print("Ha bor")
        break
else:
    print("Yo'q")
