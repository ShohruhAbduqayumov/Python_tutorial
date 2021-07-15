import datetime as dt
#
# while True:
# print(datetime.datetime.now())

# vaqt = dt.datetime.now()
#
# print(vaqt.year) # yil
# print(vaqt.month) # oy
# print(vaqt.day) # kun
# print(vaqt.weekday()) # hafta kuni 0 dan boshlanadi
# print(vaqt.hour) # soat
# print(vaqt.minute) # minut
# print(vaqt.second) # sekund
# print(vaqt.microsecond) # mikrosekund
# t = dt.datetime.now()
# def vaqt(t):
#     print(f"soat: {t.hour - 6}:{t.minute} bo'ldi")
# vaqt(t)


""" vaqtni belgilash """

x = dt.datetime(2021, 7, 15, 11, 28, 35)
print(x)
print(x.strftime("%a"))
print(x.strftime("%A"))
print(x.strftime("%b"))
print(x.strftime("%B"))

x = dt.datetime.now().second
while True:
    if x + 5 == dt.datetime.now().second:
        print("Salom")
        break