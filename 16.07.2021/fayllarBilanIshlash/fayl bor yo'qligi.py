import os
if os.path.exists("mening_faylim.txt"):
    os.remove("mening_faylim.txt")
    print("fayl o'chdi")
else:
    print("Bunday fayl mavjud emas")