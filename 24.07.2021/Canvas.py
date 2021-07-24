# 6 - misol Canvas
# oddiy shakl yaratish
from tkinter import *

asosiy_oyna = Tk()

# canvas yaratish
C = Canvas(
    asosiy_oyna, # asosiy oynada
    bg="yellow", # fon rangi
    height=500, # balandligi
    width=800 # eni
)

# chiziq yaratish
chiziq = C.create_line(100, 120, 320, 40, fill="green", width=5)

# burchak yaratish
burchak = C.create_arc(180, 150, 80, 210, start=0, extent=180, fill="red")

# oval yaratish
oval = C.create_oval(80, 30, 140, 150, fill="blue")

# canvasni asosiy oynaga joylash
C.pack()
asosiy_oyna.mainloop()