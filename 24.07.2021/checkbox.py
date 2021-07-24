# 5 - misol checkBox
from tkinter import *

# oynani qurish
asosiy_oyna = Tk()

# oynaga o'lcham
asosiy_oyna.geometry('300x400')
# label qurish
w = Label(asosiy_oyna, text="Checkbox lar", font='50')

# labelni joylash
w.pack()

# # checkboxlarni int qiymat qabul qiladigan qilib e'lon qilsih
# Checkbutton1 = IntVar()
# Checkbutton2 = IntVar()
# Checkbutton3 = IntVar()

button1 = Checkbutton(asosiy_oyna, text="qora",
                      variable=IntVar(),
                      onvalue=1,
                      offvalue=0,
                      height=5,
                      width=10)

button2 = Checkbutton(asosiy_oyna, text="yashil",
                      variable=IntVar(),
                      onvalue=1,
                      offvalue=0,
                      height=5,
                      width=10)

button3 = Checkbutton(asosiy_oyna, text="qizil",
                      variable=IntVar(),
                      onvalue=1,
                      offvalue=0,
                      height=5,
                      width=10)

button1.pack()
button2.pack()
button3.pack()

asosiy_oyna.mainloop()