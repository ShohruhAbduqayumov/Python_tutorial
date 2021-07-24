# 4 - misol

# radio button
from tkinter import *

# asosiy oynani yasash
asosiyOyna = Tk()

# o'lcham berish
asosiyOyna.geometry('400x400')

# string ma'lumotlardan foydalanish uchun
# bu yerda birinchi radio button tanlanib turadi
v = StringVar(asosiyOyna, '1')

# tugmalar qiymatlarini saqlash uchun lig'at
qiymatlar = {
    'RadioButton 1': "1",
    'RadioButton 2': "2",
    'RadioButton 3': "3",
    'RadioButton 4': "4",
    'RadioButton 5': "5"
}

# barcha tugamalarni Asosiy oynaga joylash uchun for loop
for (matn, qiymat) in qiymatlar.items():
# radio button qurish:
    tugma = Radiobutton(
        asosiyOyna,
    text=matn,
    variable=v,
    value=qiymat,
    background="white"
)
# pack(x kordinata, y kordinata)
tugma.pack(side=TOP, ipady=5)

# oynani ushlab turish uchun
asosiyOyna.mainloop()