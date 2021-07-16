# f = open("men_haqimda.txt", "w")
# f.write("Shohruh ")
# f.close()

f = open("men_haqimda.txt", "r")
print(f.read())
f.close()

f = open("men_haqimda.txt", "w")
f.write(" Abduqayumov ")
f.close()

f = open("men_haqimda.txt", "a")
f.write(" Shohruh ")
f.close()

f = open("men_haqimda.txt", "r")
print(f.read())
f.close()


# yaratish
# f = open("men_haqimda.txt", "x")

# isminni yozaman
f = open("men_haqimda.txt", 'w')
f.write("Oybek")

# konsolga chiqarish
f = open("men_haqimda.txt", 'r')
print(f.read())

# familiyamni yozaman
f = open("men_haqimda.txt", "a")
f.write("Narzullayev")

# konsolga chiqarish
f = open("men_haqimda.txt", 'r')
print(f.read())