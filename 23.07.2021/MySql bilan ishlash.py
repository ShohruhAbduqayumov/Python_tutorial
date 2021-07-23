import mysql.connector

meningMB = mysql.connector.connect(
    host="localhost",
    user="root",
    password="14122017",
    database="maktab"

)

mycursor = meningMB.cursor()

mycursor.execute("show databases")

bazalar = []

for db in mycursor:
    bazalar.append(db[0])

print(bazalar)

if "test" in bazalar:
    print("bor")
    mycursor.execute("drop database test")
    print("o'chirildi")
else:
    print("yaratildi")
    mycursor.execute("create database test")


