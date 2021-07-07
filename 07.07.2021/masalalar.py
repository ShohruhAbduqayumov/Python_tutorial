""" 1-masala. Mevalar to'plami berilgan unga gilos elementini qo'shing"""

mevalar = {"olma","anor","banan","apelsin"}
mevalar.add("gilos")

print(mevalar)

""" 2-masala. mevalar degan set elon qilasiz, ruyhatga o'tkazasiz, toifasini chop etasiz,
yana qaytarib setga o'tkazib toifasini chop etasiz
"""

mevalar = {"olma","anor","banan","apelsin"}
mevalar = list(mevalar)
print(type(mevalar))

mevalar = set(mevalar)
print(type(mevalar))

"""3-masala. ikkita element qo'shish """

mevalar = {"olma","anor","banan","apelsin"}
mevalar.update(["gilos","olcha"])
print(mevalar)

"""4-masala. """

mevalar = {"olma","anor","banan","apelsin"}
mevalar.remove("olma")
print(mevalar)

"""5-masala."""

mevalar = {"olma","anor","banan","apelsin"}
mevalar.clear()
print(mevalar)

