# """GUI -> grafik foydalanuvchi interfeysi"""
# # 1-misol
# from tkinter import *
# m = Tk() # bu biz yaratgan oyna
#
# # label yaratish
# meningLabelim = Label(m, text="Assalomu alaykum")
#
# # oynaga joylash
# meningLabelim.pack()
# m.mainloop() # oynani ushlab turish

# # 2-misol. Button yaratish
#
# from tkinter import *
#
# asosiyOyna = Tk()
#
# # oynani o'lchamini belgilash uchun
# asosiyOyna.geometry('600x400')
#
# # tugma qo'shish Button(oyna, text="matn", bd="qalinligi", command="tugma bosilgandagi hodisa")
# tugma = Button(asosiyOyna, text="Yopish", bd='10', command=asosiyOyna.destroy)
#
# # buttonni oynaga joylash
# tugma.pack()
#
# asosiyOyna.mainloop() # oynani ushlab turish uchun
#
#

# # 3-misol. Button turlari
#
# # radio button
# from tkinter import *
#
# # asosiy oynani yasash
# asosiyOyna = Tk()
#
# # o'lcham berish
# asosiyOyna.geometry('400x400')
#
# # string ma'lumotlardan foydalanish uchun
# v = StringVar(asosiyOyna, '1')
#
# # tugmalar qiymatlarini saqlash uchun lig'at
# qiymatlar = {
#     'RadioButton 1': "1",
#     'RadioButton 2': "2",
#     'RadioButton 3': "3",
#     'RadioButton 4': "4",
#     'RadioButton 5': "5"
# }
#
# # barcha tugamalarni Asosiy oynaga joylash uchun for loop
# for (matn, qiymat) in qiymatlar.items():
#     # radio button qurish:
#     tugma = Radiobutton(
#         asosiyOyna,
#         text=matn,
#         variable=v,
#         value=qiymat,
#         indicator=0,
#         background="light blue"
#     )
#     # pack(x kordinata, y kordinata)
#     tugma.pack(ipadx=100, ipady=20)
#
# # oynani ushlab turish uchun
# asosiyOyna.mainloop()

